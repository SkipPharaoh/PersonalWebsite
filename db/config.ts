import { column, defineDb, defineTable, NOW } from "astro:db";

export const PageView = defineTable({
  columns: {
    url: column.text(),
    date: column.date(),
  },
  indexes: {
    url_idx: { on: ["url"], unique: false },
    date_idx: { on: ["date"], unique: false },
  },
});

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
  },
  indexes: {},
});

export const UserGeoLocation = defineTable({
  columns: {
    geo_id: column.number({ primaryKey: true }),
    user_id: column.text({ unique: false }),
    country: column.text(),
    region: column.text(),
    city: column.text(),
    latitude: column.number({ optional: true }),
    longitude: column.number({ optional: true }),
    timezone: column.text({ optional: true }),
    zipcode: column.text({ optional: true }),
  },
  indexes: {},
});

export default defineDb({
  tables: { PageView, UniquePageViews, UserGeoLocation },
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
device_type: Type of device used (e.g., desktop, mobile, tablet).
browser: Browser used by the device (e.g., Chrome, Firefox, Safari).
os: Operating system of the device (e.g., Windows, macOS, Android, iOS).
event_type: The type of event being tracked (e.g., page view, button click, purchase, etc.).
timestamp: Timestamp indicating when the event occurred.
url: page URL for page views.

2) GeoLocation Table (optional):

geo_id: Primary key, a unique identifier for each geographical location.
user_id: Foreign key referencing the PageViews Table, representing the user associated with the location.
country: Country of the user.
region: Region or state of the user.
city: City of the user.
latitude: Latitude coordinate of the user's location.
longitude: Longitude coordinate of the user's location.
timezone: Timezone of the user.
zipcode: Postal code of the user.

*/
