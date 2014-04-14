%% Matlab and NetCDF
% Written by:   Shelley Knuth
% Affiliation:  Research Computing, CU-Boulder
% Date:         28 February 2014
% Purpose:      The purpose of this program is to work with NetCDF data in
% Matlab, including both reading and writing.
% The file we will use is sample_data.nc, which was a sample of data
% downloaded from Unisys that contains model precipitation data at various
% levels.

%% Inputs

    % Set a variable defining the location of our test data
    source='/Users/knuths/Documents/MATLAB/test_data/sample_data.nc';


%% Get info about NetCDF data
    %% Display basic information on the netCDF file

    % Includes information on the structure, number of
    % dimensions and variables, etc.  
    finfo=ncinfo(source);
    disp(finfo)

    %% Dimensions

    % What are the names of the dimensions?
    dimNames={finfo.Dimensions.Name}
    % This result shows that there are five dimensions:  lat, lon, bnds, plev,
    % and time.  


    % To find more information on each dimension, type:
    dimInfo_plev=ncinfo(source,'plev')
    % This tells me that the data is double, with a size of 17 and is written
    % in classic NetCDF

    %% Variables

    % Variable information
    varNames={finfo.Variables.Name}
    % This tells me that there are 12 variables

%%  Get all information about variable
    ncdisp(source,'tas')
    % This gives us all the information about the groups, dimensions, etc.
    
%     ncdisp(source)
    % Gives you all the information about the dataset
    
%% Read Just the Attributes

    % The attribute conventions are as follows:
    %units, long_name, _FillValue, missing_value, valid_min, valid_max,
    %valid_range, scale_factor, add_offset, signedness, C_format,
    %FORTRAN_format, title, history, Conventions

    % Each dataset isn't required to have these variables, so results may vary

    % Get long name of the 9th variable in varNames ('tas')
    ncreadatt(source,'tas','long_name')

    % Get units of the 9th variable in varNames ('tas')
    ncreadatt(source,'tas','units')


%% Read in NetCDF data

    % Let's read in the temperature data from the file
    temp_data=ncread(source,'tas')

    
    