<span id = 'top'></span>
<a href='https://github.com/shivamkapasia0' target="_blank"><img alt='python' src='https://img.shields.io/badge/Python-100000?style=for-the-badge&logo=python&logoColor=FFFF00&labelColor=0C86EA&color=FFFFFF'/></a>
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=black)
![Power BI](https://img.shields.io/badge/PowerBI-000000?style=for-the-badge&logo=Power%20BI&logoColor=yellow)
<a href='https://github.com/shivamkapasia0' target="_blank"><img alt='Numpy' src='https://img.shields.io/badge/numpy-100000?style=for-the-badge&logo=Numpy&logoColor=2291A9&labelColor=FFFFFF&color=FFFFFF'/></a>
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

---

---

<h1><details><summary><i>📌 Contents</i></summary>

### [1. Introduction](#introduction)

### [2. Context](#context)

### [3. Objectives](#objectives)

### [4. Conclusion](#conclusion)

</details></h1>

# Introduction

Internet has become a key part of our lives since its creation. So much so, that without access to the Internet, you are completely off the grid. <br>

Internet access and high-speed connection go hand in hand with the seamless flow of information, empowering individuals and businesses to explore, communicate, and innovate in the digital age.

We set ourselves to explore the quantity and quality of Argentina's Internet infrastructure. Looking at data from the years 2014 to 2022 from the official [ENACOM Website](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/) (National Communications Agency in Argentina)

What we did for this particular case, was to extract all the data available for us and transform it before we used it.

- ETL process: we transformed the data we had - deleting null values, duplicates, outliers or any other data that had no relevance to our case of study - in order to fit our needs, with technologies like Pandas, Matplotlib and Seaborn.

- EDA process: Once our data was cleaned and ready to be used, we proceeded to plot it to see if there was any pattern or clue that could lead us to our goal. To further improve our insights, we gathered news such as [this article](https://www.clarin.com/economia/teletrabajo-pandemia-medio-millon-hogares-contrato-internet_0_nn6f0GHvOT.html) to have a better understanding in case we didn't expect our results to be the way that we expected.

# Context

![Logo](./assets/images/logo.jpg)

#### In this project, we simulate the role of a Data Analyst for a company called '**Glide**'. We were hired by the company to gather data about what difficulties Argentina faces and how can we turn the odds in the country's favour as well as the company's.

<br>

# Objectives

#### Glide's main goal is to focus all efforts on getting a 2% raise on Internet access on the next quarter per 100 inhabitants for each province. Apart from that, another vital target is to increase the number of wireless connection. Despite being one of the most popular technologies, the lack of wireless networks in Argentina is surprisingly high, especially in the northern part of the country.

#### To achieve this, we measured two different KPIs:

1. KPI = ((newAccess - currentAccess) / currentAccess) \* 100 <br>
   where:

- `newAccess` refers to the number of households with Internet access after the next quarter
- `currentAccess` refers to the number of households with internet access in the present quarter

![Internet Access per 100 houses per year](./assets/images/internet_access_per_100_houses_per_year.png)
As we see in the previous image, Internet access has seen a non-stop increase in recent years, and with the help of our performance indicator we can know exactly how much this increase represents, year by year and quarter by quarter.

2. KPI = ((nextQuarterWirelessConnection - currentQuarterWirelessConnection) / currentQuarterWirelessConnection) \* 100 <br>
   where:

- `nextQuarterWirelessConnection` refers to the number of households with wireless connection after the next quarter
- `currentQuarterWirelessConnection` refers to the number of households with wireless connection in the present quarter
  ![Wireless Connections](./assets/images/pie_wireless.png)
  Wireless connections for the year 2021
  ![Wireless Connections](./assets/images/pie_wireless_2.png)
  Wireless connections for the year 2022

As wee see, wireless connections increased from the year 2021 to the year 2022. We wanted to know how much did increase and, if possible, make that increment greater.

# Conclusion

Thanks to our exhaustive analysis of the data and its subsequent visualization through PowerBI we discovered that Internet connections did increase a 2%, even more in some cases, as well as less than 2% from various types of connections. Nevertheless, there is an obvious trend of increasing the access throughout the whole country.

<a href = #top >Back to the Top</a>
