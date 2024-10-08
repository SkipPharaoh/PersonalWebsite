---
title: Personal Reading Trends
publishDate: 2023-01-01 00:00:00
img: /assets/stock-3.jpg
img_alt: Open book with pages flared
description: |
  This is a compilation of the books i've read since 2021; presented in a PowerBi Dashboard
tags:
  - Python
  - PowerBi
  - Personal Growth
permalink: https://github.com/Sonya-7/Reading_List
---

## Project Description
This project showcases a comprehensive collection of books I have read since January 2021. It presents engaging word clouds and an interactive dashboard, offering a captivating visualization of my literary journey.

This project serves as a means to meticulously trace the words that have shaped my mind throughout the year. It is intriguing to note that, according to a Statistica survey, on average, Americans read 12 books annually, with 65% of them being print books. This statistic surpassed my initial expectations and inspired me to delve into a broader range of literature, setting the goal of reading at least 1 book per month.

Furthermore, in recognizing the profound influence of language in our daily lives, I am devoted to purposefully incorporating specific words and ideas into my consciousness on a daily basis. This endeavor is a deliberate effort to enhance my awareness and expand my intellectual horizons.

By combining my passion for data science with my love for learning, this project displays my technical expertise and commitment to personal growth.

### Preview of ELT Insights
<p id="reading-trends" style="justify-content: center; gap: 10px;">
  <img src="https://github.com/Sonya-7/Reading_List/assets/92489108/be37116e-6731-415b-bbdf-587ae3491e5f" width="358" height="255"/>
  <img src="https://github.com/Sonya-7/Reading_List/assets/92489108/b69c3377-a4b5-4921-8584-c8613b6fa833" width="358" height="255"/>
</p>

### Preview of Word Clouds Containing Dominant Words in Book Titles
<p align="center">
  <img src="https://github.com/user-attachments/assets/87230daf-9b75-4e25-bd58-4fb3009ea91e" width="358" height="50%"/>
  <!-- <img src="https://github.com/Sonya-7/Reading_List/assets/92489108/e0f20fa1-a1f6-4206-80de-01f4a3615bfd" width="358" height="50%"/> -->
</p>

### Preview of PowerBi Dashboard
<p align="center">
  <img src="https://github.com/Sonya-7/Reading_List/assets/92489108/ea74cd45-7fa1-4bdf-b02a-a088532a2e79" width="353" height="50%"/>
</p>

<script>
  function applyResponsiveStyle() {
    const p = document.getElementById('reading-trends');
    if (window.innerWidth <= 730) {
      p.style.display = 'block';
      p.style.textAlign = "center";
    } else {
      p.style.display = 'flex';
    }
  }

  // Apply the style on initial load
  applyResponsiveStyle();

  // Apply the style on window resize
  window.addEventListener('resize', applyResponsiveStyle);
</script>