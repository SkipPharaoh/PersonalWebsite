export const prerender = false;

import type { APIRoute } from "astro";
import { PageView, eq, db, count, UniquePageView, GeoLocation } from "astro:db";

// This is a DB endpoint that returns a JSON for the views count
// Read more about Astro DB in the Astro docs:
// https://docs.astro.build/en/guides/astro-db/#query-your-database
export const GET: APIRoute = async ({ request }) => {
  const url = new URL(request.url).pathname;

  if (!url) {
    return new Response(
      JSON.stringify({
        error: "Missing URL",
      }),
      { status: 400 }
    );
  }

  const uniqueCount = await db.select().from(UniquePageView);
  const location = await db.select().from(GeoLocation);
  const viewCount = await db
    .select({ value: count() })
    .from(PageView)
    .where(eq(PageView.url, url));

  return new Response(
    JSON.stringify({
      count: viewCount[0]?.value,
      uniqueCount,
      location,
    }),
    {
      status: 200,
      headers: {
        "Cache-Control": "s-maxage=3600, stale-while-revalidate",
      },
    }
  );
};
