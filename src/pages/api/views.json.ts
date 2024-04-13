export const prerender = false;

import type { APIRoute } from "astro";
import { PageView, eq, db, count } from "astro:db";

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

  const viewCount = await db
    .select({ value: count() })
    .from(PageView)
    .where(eq(PageView.url, url));
  return new Response(
    JSON.stringify({
      count: viewCount[0]?.value,
    }),
    {
      status: 200,
      headers: {
        "Cache-Control": "s-maxage=3600, stale-while-revalidate",
      },
    }
  );
};

// This is the Search Endpoint (API Route) for the page_views database on vercel
// Read more about Search Endpoint (API Route) in the Astro docs:
// https://docs.astro.build/en/guides/endpoints/#server-endpoints-api-routes

// const viewCount = await db
//   .select({ value: count() })
//   .from(PageView)
//   .where(eq(PageView.url, url));

// export const GET: APIRoute = async ({ params, request }) => {
//   const res = await sql`SELECT * FROM page_views`;
//   // const res = await fetch(import.meta.env.POSTGRES_URL);
//   // if (!res) {
//   //   return new Response(null, {
//   //     status: 404,
//   //     statusText: "Not found",
//   //   });
//   // }
//   // const views = await fetch(import.meta.env.POSTGRES_URL);
//   return new Response(
//     JSON.stringify({
//       name: "Astro",
//       res,
//       // views,
//       url: "https://astro.build/",
//     })
//   );
// };
