---
title: Personal Reading Trends
publishDate: 2025-01-01 00:00:00
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
   <img  src="https://github.com/user-attachments/assets/daedca24-992b-4439-be21-a779e2e7e51e" width="358" height="255"/>
   
  <img  src="https://github.com/user-attachments/assets/cb82865b-8184-4d86-9162-799aea122456" width="358" height="255"/>
</p>

### Preview of Word Clouds Containing Dominant Words in Book Titles

<p align="center">
    <img  src="https://github.com/user-attachments/assets/5d71f38c-384d-465d-bc15-df870bbd7bf7" width="458" height=255/>
  <!-- <img src="https://github.com/Sonya-7/Reading_List/assets/92489108/e0f20fa1-a1f6-4206-80de-01f4a3615bfd" width="358" height="50%"/> -->
</p>

### Preview of PowerBi Dashboard

<p align="center">
     <img  src="https://github.com/user-attachments/assets/9c1f45b1-fa43-4bea-8bf7-66ecb91cc94b" width="588" height=355/>
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
