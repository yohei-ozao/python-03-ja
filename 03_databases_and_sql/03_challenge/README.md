# Challenge 3: Track Length Buckets

This challenge involves categorizing the length of music tracks into buckets.

- Implement **`track_length_buckets`** to categorize tracks based on their duration.
- The width of each bucket should be **1 minute** (60000 milliseconds in the Chinook database, as track durations are stored in milliseconds).
- For example, the bucket **1** will contain the count of all tracks with a duration between **0** and **60000** milliseconds.
- This method should return a list of tuples like (**`max_duration_in_minutes`**, **`track_count`**).