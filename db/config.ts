import { column, defineDb, defineTable, NOW } from "astro:db";

export const UniquePageViews = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    user_id: column.text({ unique: false }),
    session_id: column.text({ unique: false }),
    device_id: column.text({ unique: false }),
    user_device_info: column.text({ unique: false }),
    browser: column.text({ unique: false }),
    event_type: column.text({ unique: false }),
    timestamp: column.date({ default: NOW }),
    url: column.text({ unique: false }),
    city: column.text({ optional: true, unique: false }),
    country: column.text({ optional: true, unique: false }),
    region: column.text({ optional: true, unique: false }),
    flag: column.text({ optional: true, unique: false }),
    countryRegion: column.text({ optional: true, unique: false }),
    latitude: column.number({ optional: true, unique: false }),
    longitude: column.number({ optional: true, unique: false }),
  },
  indexes: {},
});

export default defineDb({
  tables: { UniquePageViews },
});

/**
 * 
Since this is for the Unique views of the users, we can use one table for now. if we need any other data, we can add others then.
User ids can be created based on Browser Fingerprinting (BF). BF is a method of identifying and tracking users based on the unique characteristics of their web browser and device configuration. Instead of relying on personally identifiable information like IP addresses, browser fingerprinting generates a unique fingerprint based on factors such as:
    - User Agent: Information about the user's browser, operating system, and device.
    - Browser Configuration: Details about browser settings, installed plugins, and fonts.
    - Screen Resolution: The size and resolution of the user's screen.
    - Timezone: The user's timezone, which can provide additional contextual information.
By combining these factors, browser fingerprinting can create a unique identifier for each user, even if they don't log in or provide explicit personal information

1) Unique PageViews Table:

user_id: Primary key, a unique identifier for each user.
session_id: The unique identifier for each session.
device_id: The unique identifier for each device.
user_device_info: Info of the device: device type, os, etc.
browser: Browser used by the device (e.g., Chrome, Firefox, Safari).
event_type: The type of event being tracked (e.g., page view, button click, purchase, etc.).
timestamp: Timestamp indicating when the event occurred.
url: page URL for page views.
city: City of the user.
country: Country of the user.
region: Region or state of the user.
flag: Country flag emoji of user's location.
countryRegion: The region part of the ISO 3166-2 code of the client IP.
latitude: Latitude coordinate of the user's location.
longitude: Longitude coordinate of the user's location.

*/
