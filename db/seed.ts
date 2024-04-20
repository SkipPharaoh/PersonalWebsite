import { db, PageView, UniquePageView, GeoLocation } from "astro:db";

export default async function () {
  await db.insert(PageView).values([
    { date: new Date(), url: "/" },
    { date: new Date(new Date().getTime() - 1000), url: "/test" },
  ]);

  await db.insert(UniquePageView).values([
    {
      user_id: 1,
      session_id: "session123",
      device_id: "device456",
      device_type: "desktop",
      browser: "Chrome",
      os: "Windows",
      event_type: "page view",
      timestamp: new Date("2024-04-19T09:30:00Z"),
      url: "http://example.com/page1",
    },
    {
      user_id: 2,
      session_id: "session456",
      device_id: "device789",
      device_type: "mobile",
      browser: "Safari",
      os: "iOS",
      event_type: "page view",
      timestamp: new Date("2024-04-19T10:15:00Z"),
      url: "http://example.com/page2",
    },
    {
      user_id: 3,
      session_id: "session789",
      device_id: "device012",
      device_type: "tablet",
      browser: "Firefox",
      os: "Android",
      event_type: "page view",
      timestamp: new Date("2024-04-19T11:00:00Z"),
      url: "http://example.com/page3",
    },
  ]);

  await db.insert(GeoLocation).values([
    {
      geo_id: 1,
      user_id: 1,
      country: "USA",
      region: "California",
      city: "San Francisco",
      latitude: 37.7749,
      longitude: -122.4194,
      timezone: "PST",
      zipcode: "94102",
    },
    {
      geo_id: 2,
      user_id: 2,
      country: "UK",
      region: "England",
      city: "London",
      latitude: 51.5074,
      longitude: -0.1278,
      timezone: "GMT",
      zipcode: "SW1A",
    },
    {
      geo_id: 3,
      user_id: 3,
      country: "Japan",
      region: "Tokyo",
      city: "Shinjuku",
      latitude: 35.6895,
      longitude: 139.6917,
      timezone: "JST",
      zipcode: "160-0023",
    },
  ]);
}
