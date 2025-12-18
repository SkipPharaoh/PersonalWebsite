import db from "@astrojs/db";
import vercel from "@astrojs/vercel/serverless";
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  output: "server",
  adapter: vercel({
    edgeMiddleware: true,
    functionPerRoute: false,
    runtime: "nodejs20.x", // Add this line
  }),
  integrations: [db()],
});
