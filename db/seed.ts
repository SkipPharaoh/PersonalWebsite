import { db, PageView, UniquePageViews, UserGeoLocation } from "astro:db";

export default async function () {
  await db.insert(PageView).values([
    { date: new Date(), url: "/" },
    { date: new Date(new Date().getTime() - 1000), url: "/test" },
  ]);

  await db.insert(UniquePageViews).values([
    {
      id: 1,
      user_id: "user123",
      session_id: "session123",
      device_id: "device123",
      user_device_info:
        "(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
      browser: "Arc",
      event_type: "Unique Page View",
      timestamp: new Date("2024-04-19T09:30:00Z"),
      url: "http://example.com/page1",
    },
    {
      id: 2,
      user_id: "user456",
      session_id: "session456",
      device_id: "device456",
      user_device_info:
        "(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
      browser: "Brave",
      event_type: "Unique Page View",
      timestamp: new Date("2024-04-19T10:15:00Z"),
      url: "http://example.com/page2",
    },
    {
      id: 3,
      user_id: "user789",
      session_id: "session789",
      device_id: "device789",
      user_device_info:
        "(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
      browser: "Chrome",
      event_type: "Unique Page View",
      timestamp: new Date("2024-04-19T11:00:00Z"),
      url: "http://example.com/page3",
    },
  ]);

  await db.insert(UserGeoLocation).values([
    {
      geo_id: 1,
      user_id: "user123",
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
      user_id: "user456",
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
      user_id: "user789",
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
