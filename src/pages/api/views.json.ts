export const prerender = false;

import type { APIRoute } from "astro";
import { count, db, eq, UniquePageViews } from "astro:db";
import { isbot } from "isbot";

// This is a DB endpoint that returns a JSON for the views count
// Read more about Astro DB in the Astro docs:
// https://docs.astro.build/en/guides/astro-db/#query-your-database
export const GET: APIRoute = async ({ request }) => {
  if (isbot(request.headers.get("user-agent"))) {
    return new Response(
      JSON.stringify({
        error: "This endpoint is not available for bots",
      }),
      { status: 401 }
    );
  }

  const url = new URL(request.url).pathname;

  if (!url) {
    return new Response(
      JSON.stringify({
        error: "Missing URL",
      }),
      { status: 400 }
    );
  }

  const uniqueCount = await db.select().from(UniquePageViews);
  const viewCount = await db
    .select({ value: count() })
    .from(UniquePageViews)
    .where(eq(UniquePageViews.id, UniquePageViews.id));

  return new Response(
    JSON.stringify({
      count: viewCount[0]?.value,
      uniqueCount,
    }),
    {
      status: 200,
      headers: {
        "Cache-Control": "s-maxage=3600, stale-while-revalidate",
      },
    }
  );
};
