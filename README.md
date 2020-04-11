# Covid19Stats

**Covid19Stats** is a Python program that works with the csv files that are provided by [data.humdata](https://data.humdata.org). The csv files can be downloaded from [Covid-19 Cases Data](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases).

## Availability
 
The program runs on Windows, Linux and Mac operating systems.

## Dependencies

In order to run **Covid19Stats**, at least [Python](https://www.python.org/)'s 3.6 version must be installed on your computer. Note that in order to use [Python](https://www.python.org/) on the command prompt, [Python](https://www.python.org/) should be added to the PATH.

There are several libraries that the program requires. In order to install these requirements users should type the below command on console window.

```
pip3 install -r requirements.txt
```

## Usage

**For Linux and Mac**

```
python3 Covid19Stats.py
```

**For Windows**
```
python Covid19Stats.py
```

## Screenshots

1. Below is the main screen when the program opens.

![img1](https://user-images.githubusercontent.com/29302909/79031212-e5983800-7ba5-11ea-8076-f92407430f6c.png)

2. When users select a country and right click on treeview, a right click menu will be created. 

![img2](https://user-images.githubusercontent.com/29302909/79031421-2e9cbc00-7ba7-11ea-806f-ef3500110653.png)

3. If users extend the **View Case Graphs** cascade, three options which are named as **Confirmed**, **Deaths** and **Recovered** will be created. And if one of these options is selected, the graph of the selected option will be displayed.

![img3](https://user-images.githubusercontent.com/29302909/78509888-19d0ba80-779a-11ea-8d75-edcdafa036d1.png)

4. If users extend the **View Proportion Graphs** cascade, three options which are named as **Deaths/Confirmed**, **Recovered/Confirmed** and **Recovered/Deaths** will be created. And if one of these options is selected, the graph of the selected option will be displayed.

![img4](https://user-images.githubusercontent.com/29302909/78509889-1ccbab00-779a-11ea-8b97-7843259880ff.png)

5. If users extend the **View Increase Rate** cascade, three options which are named as **Confirmed**, **Deaths** and **Recovered** will be created. And if one of these options is selected, a treeview of the selected option will be displayed.

![img5](https://user-images.githubusercontent.com/29302909/78509893-1fc69b80-779a-11ea-9852-effecb211e92.png)

6. Users can also select multiple countries and can look at the case and proportion graphs and also the increase rate of values per day. In this case, the values per day of the selected countries will be summed and will be used as a single data. However if users select at least 2 and at most 5 countries, they can use **Compare Case Graphs** and **Compare Proportion Graphs** cascades. These cascades have the same options that the **View Case Graphs** and **View Proportion Graphs** have. The difference is that the values of the selected countries will be inserted to the graphs one by one. And these graphs look a bit different than the other graphs.

![img6](https://user-images.githubusercontent.com/29302909/79031419-2ba1cb80-7ba7-11ea-9ab4-8e0d0c522f56.png)

![img7](https://user-images.githubusercontent.com/29302909/78509904-2ead4e00-779a-11ea-834a-5d7e0ce99958.png)

7. Users can also use the other options for the selected planets.

![img8](https://user-images.githubusercontent.com/29302909/78509907-3240d500-779a-11ea-9ae1-5029f086ace6.png)

8. Users can also select all countries and can use the all right click options except from the cascades that are related to comparing. As mentioned above, the comparing feature is only valid for at least 2 and at most 5 selected countries. The names of the countries won't be written to the graph and treeview title, instead the number of the selected countries will be written as a title.

![img9](https://user-images.githubusercontent.com/29302909/79031213-e7fa9200-7ba5-11ea-9690-b72867c3103e.png)

![img11](https://user-images.githubusercontent.com/29302909/78509919-44227800-779a-11ea-95b8-fac42b7087e4.png)

![img12](https://user-images.githubusercontent.com/29302909/78509920-47b5ff00-779a-11ea-9234-1909aeca9566.png)

![img13](https://user-images.githubusercontent.com/29302909/78509923-4b498600-779a-11ea-9f9e-4b437fa97a98.png)
