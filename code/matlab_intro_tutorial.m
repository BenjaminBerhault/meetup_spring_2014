%% Matlab Tutorial
% Written by:   Shelley Knuth (shelley.knuth@colorado.edu)
% Affiliation:  Research Computing, CU-Boulder
% Date:         27 February 2014
% Purpose:      The purpose of this program is to practice reading in and
% plotting various types of data for a tutorial.  We will be reading in
% weather data that was produced on February 1, 2014 at five different
% times.  The in the file is date, time, temperature, pressure, relative
% humidity (RH), and wind speed.  The location of the data is at various
% weather stations (ARN, BRN, CRN).  The test files are named:
% 20140201_stnARN.txt, 20140201_stnBRN.csv, and 20140201_stnCRN.xlsx

%% Clear any previous variables
clear;
%% Manual inputs
% Let's set up some manual inputs that we can use later when we read in the
% data and plot it

date=20140201;  % The date in the file names given above
datef=int2str(date);  % Convert the integer to a string to input into file names
station1='ARN';  % The quotes make it a string
station2='BRN';
station3='CRN';

%% Read in ASCII text data
% Matlab can read in various types of data.  Let's first test this with
% ASCII text data.  

% Open the file and assign an id
fid=fopen(strcat('/Users/knuths/Documents/MATLAB/test_data/',datef,'_stn',station1,'.txt'),'r'); 

% The data files are:
% 20140201_stnARN.txt
% 20140201_stnBRN.csv
% 20140201_stnCRN.xls

% Read in the data
% Here, we have six columns of floating point data.  The first row is a header
% Also, our time data has a character (:) in it, so must be read in as a
% string
A=textscan(fid,'%f%s%f%f%f%f','HeaderLines',1);

% We can assign variables to each of the six columns if we wish.  This step
% is not necessary, but will make it easier for coding later.

datea=A{1};
timea=A{2};
tempa=A{3};
pressurea=A{4};
rha=A{5};
windsa=A{6};

% Close the open file
fclose(fid);

%% Read in CSV data
% Let's next test this with CSV data.  

% Open the file and assign an id
fid1=fopen(strcat('/Users/knuths/Documents/MATLAB/test_data/',datef,'_stn',station2,'.csv'),'r'); 

% Another way to read CSV files is with csvread - however, you cannot read
% alphanumeric data.  Therefore, if you have both data and strings, 
% you will need to use fopen.

% Assign variables
B=textscan(fid,'%f%s%f%f%f%f','Delimiter',',','HeaderLines',1);

dateb=B{1};
timeb=B{2};
tempb=B{3};
pressureb=B{4};
rhb=B{5};
windsb=B{6};

% Close the open file
fclose(fid1);

%% Read in XLSX data
% Let's next test this with XLSX data.  

% Open the file and assign an id
[datac,headertext]=xlsread(strcat('/Users/knuths/Documents/MATLAB/test_data/',datef,'_stn',station3,'.xlsx'),'datac'); 

% You can read in multiple tabs of Excel data.  Each tab is assigned by
% name with the same synax as above (but the second datac is changed to
% reflect the name of the tab in the Excel file if you wanted to read in another value).

datec=datac(:,1);
timec_orig=datac(:,2);
tempc=datac(:,3);
pressurec=datac(:,4);
rhc=datac(:,5);
windsc=datac(:,6);
    
%% Convert strings to numbers to plot

timea_num=zeros(length(timea),1);  % We define our variable and size.  Not necessary, but program will run faster

for i=1:length(timea)
    timea_num(i)=str2double(strrep(timea(i),':',''));
end

timeb_num=zeros(length(timeb));  % We define our variable and size.  Not necessary, but program will run faster

for i=1:length(timeb)
    timeb_num(i)=str2double(strrep(timeb(i),':',''));
end

% The time data in column 2 for the XLS data has been converted to a number.  We need to use datestr to
% convert it back.  The cellstr converts the variable to a string.

for i=1:length(timec_orig)
    timec(i)=cellstr(datestr(timec_orig(i),'HH:MM'));
end
    timec=timec(:);  % This transposes the data from a row to a column

timec_num=zeros(length(timec));  % We define our variable and size.  Not necessary, but program will run faster

for i=1:length(timec)
    timec_num(i)=str2double(strrep(timec(i),':',''));
end
%% Generate a simple plot

% Plot a line graph
X1=plot(timea_num(:,1),tempa);

% Plot the x and y axis labels and a title
xlabel('Hour');
ylabel('Temperature (^oC)');
title('Temperature on 1 February 2014');

% Add another set of data to the graph.  Make the line red
hold on;
X2=plot(timeb_num(:,1),tempb,'r');

% Add another set of data to the graph.  Make the line black
hold on;
X3=plot(timec_num(:,1),tempc,'k');

% Add a legend
leg=legend([X1 X2 X3],'Plot A','Plot B','Plot C');
set(leg,'Location','West');

%% Generate a simple plot

% Plot a histogram of all the temperature data

figure;  % Open a new figure window

% Create a variable with all the temperature data
temp_all=[tempa;tempb;tempc];  % The semi-colons in the array put all the data in one column

% Define the temp bins
tempBins=[-18:3:18];

% Plot a line graph
hist(temp_all,tempBins);
grid on;

% Plot the x and y axis labels and a title
xlabel('Temperature (^oC)');
ylabel('Number of Occurrences');
title('Temperature on 1 February 2014');

%% Generate a simple plot

% Plot a bar graph

figure;  % Open a new figure window

% Plot a line graph
X1=bar(timea_num(:,1),tempa);
grid on;

% Plot the x and y axis labels and a title
xlabel('Hour');
ylabel('Temperature (^oC)');
title('Temperature on 1 February 2014');

% Add another set of data to the graph.  Make the data red
hold on;
bar(timeb_num(:,1),tempb);

% Add another set of data to the graph.  Make the data black
hold on;
bar(timec_num(:,1),tempc);

h=findobj(gca,'Type','patch');
set(h(3),'FaceColor','b');
set(h(2),'FaceColor','r');
set(h(1),'FaceColor','k');

% Add a legend
leg_bar=legend([h(3) h(2) h(1)],'Plot A','Plot B','Plot C');
set(leg_bar,'Location','SouthEast');
