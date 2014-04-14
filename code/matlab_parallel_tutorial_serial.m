%% matlab_parallel_tutorial_serial.m
% Written by:   Shelley Knuth (shelley.knuth@colorado.edu)
% Affiliation:  Research Computing, CU-Boulder
% Date:         24 March 2014
% Purpose:      The purpose of this program is to demonstrate how to take
% normal Matlab code and convert it to run in parallel.

%% First we will execute simple code to run a simple mathematical function.  
% The purpose here is to test how long it takes to run the code serially.


    % Clear out all previous variables
    clear;

    % Start Matlab's stopwatch timer to measure the elapsed time
    tic;

    % Write some code to do a simple math command on a large array

    x=zeros(1000,10);
    for i=1:1000
        for j=1:10
            x(i,j)=i*(i+1)*(j-1);
        end
        y=primes(x(i,j));
    end

% Display the time elapsed since tic was executed
    toc;