import { db, UniquePageViews } from "astro:db";

export default async function () {
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
      city: "San Francisco",
      country: "USA",
      region: "California",
      flag: "🇺🇸",
      countryRegion: "USA - California",
      latitude: 37.7749,
      longitude: -122.4194,
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
      city: "London",
      country: "UK",
      region: "England",
      flag: "🇬🇧",
      countryRegion: "UK - England",
      latitude: 51.5074,
      longitude: -0.1278,
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
      city: "Shinjuku",
      country: "Japan",
      region: "Tokyo",
      flag: "🇯🇵",
      countryRegion: "Japan - Tokyo",
      latitude: 35.6895,
      longitude: 139.6917,
    },
  ]);
}
