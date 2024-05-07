export const prerender = false;

import { geolocation, ipAddress } from "@vercel/edge";
import type { APIContext, APIRoute, AstroCookies } from "astro";
import { db, UniquePageViews } from "astro:db";
import crypto from "crypto";
import { isbot } from "isbot";

interface UniquePageViewType {
  user_id: string;
  session_id: string;
  device_id: string;
  user_device_info: string;
  browser: string;
  event_type: string;
  timestamp: Date;
  url: string;
  city?: string;
  country?: string;
  region?: string;
  flag?: string;
  countryRegion?: string;
  latitude?: number;
  longitude?: number;
}

const userDataCache: Record<string, string> = {};

function generateSHA256HashString(str: string): string {
  return crypto.createHash("sha256").update(str).digest("hex");
}

function getIdFromCacheOrCookies(
  idString: string,
  idName: string,
  cookies: AstroCookies
) {
  const isSessionId = idName === "session-id";
  const isIDInCookies = cookies.has(idName);
  /**
   * the sessionExp consists of different number that make up the expiration in milliseconds
   *  - 14 days, 24 hours, 60 secs, 60 mins, 1000 is the seconds to milliseconds conversion
   */
  const sessionExpiration = 14 * 24 * 60 * 60 * 1000;

  if (!userDataCache[idString]) {
    userDataCache[idString] = generateSHA256HashString(idString);
  }

  if (!isIDInCookies) {
    cookies.set(idName, userDataCache[idString], {
      httpOnly: true,
      expires: isSessionId
        ? new Date(Date.now() + sessionExpiration)
        : undefined,
    });
  }

  return userDataCache[idString];
}

// This is a DB endpoint that returns a JSON for the views count
// Read more about Astro DB in the Astro docs:
// https://docs.astro.build/en/guides/astro-db/#query-your-database
export const POST: APIRoute = async ({
  request,
  cookies,
  clientAddress,
}: APIContext) => {
  const { screenWidth, screenHeight, pixelRatio } = await request.json();
  const screenResolution = `${screenWidth}x${screenHeight}`;
  const url = request.headers.get("referer") as string;
  const browser = request.headers.get("sec-ch-ua") as string;
  const userAgent = request.headers.get("user-agent");
  const acceptLanguage = request.headers.get("accept-language");
  const acceptEncoding = request.headers.get("accept-encoding");
  const fingerprintString = `${userAgent}${acceptLanguage}${acceptEncoding}${clientAddress}`;
  const deviceIdString = `${userAgent}${screenResolution}${pixelRatio}`;
  const userId = getIdFromCacheOrCookies(fingerprintString, "user-id", cookies);
  const deviceId = getIdFromCacheOrCookies(
    deviceIdString,
    "device-id",
    cookies
  );
  const sessionId = getIdFromCacheOrCookies(
    `${fingerprintString}${deviceIdString}`,
    "session-id",
    cookies
  );

  const { city, country, flag, countryRegion, region, latitude, longitude } =
    geolocation(request);
  const ipInfo = ipAddress(request);

  const UniquePageViewObject: UniquePageViewType = {
    user_id: userId,
    session_id: sessionId,
    device_id: deviceId,
    user_device_info: userAgent as string,
    browser,
    event_type: "Unique Page Views",
    timestamp: new Date(),
    url,
    city,
    country,
    region,
    flag,
    countryRegion,
    latitude: latitude !== undefined ? parseFloat(latitude) : undefined,
    longitude: longitude !== undefined ? parseFloat(longitude) : undefined,
  };

  if (isbot(userAgent)) {
    return new Response(
      JSON.stringify({
        error: "This endpoint is not available for bots",
      }),
      { status: 401 }
    );
  }

  if (!url) {
    return new Response(
      JSON.stringify({
        error: "Missing URL",
      }),
      { status: 400 }
    );
  }

  if (url === "api/views.json") {
    return new Response(
      JSON.stringify({
        error: "This url is not tracked",
      }),
      { status: 406 }
    );
  }

  try {
    console.log({
      headers: request.headers,
      clientAddress,
      cookies,
      UniquePageViewObject,
      ipInfo,
    });

    await db.insert(UniquePageViews).values(UniquePageViewObject);
  } catch (error) {
    error instanceof Error && console.error(error);
    return new Response(
      JSON.stringify({
        error: "Error updating views",
      }),
      { status: 400 }
    );
  }

  return new Response(
    JSON.stringify({
      message: "Succesfully updated views",
      UniquePageViewObject,
    }),
    { status: 200 }
  );
};

export const config = {
  runtime: "edge",
};
