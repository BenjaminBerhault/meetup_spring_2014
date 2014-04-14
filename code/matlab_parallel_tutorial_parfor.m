 %% matlab_parallel_tutorial_parfor.m
% Written by:   Shelley Knuth (shelley.knuth@colorado.edu)
% Affiliation:  Research Computing, CU-Boulder
% Date:         24 March 2014
% Purpose:      The purpose of this program is to demonstrate how to take
% normal Matlab code and convert it to run in parallel.


%% Let's now adjust the above the commands to run in parallel.  We will also
% want to compare our time when running serially to the time below when
% running in parallel.

    %% Let's adjust the above code to run this in parallel on my laptop
    % My laptop is a Quad Core, so it has four processors.   We can run
    % parallel processes by opening a pool with a specific number of
    % workers (which would match up to how many cores you have available to
    % you), or by using the default.
    
    % You can determine the number of cores your machine has by:
    feature('numcores')

    
    % To specify the number of workers in our pool, we use matlabpool
    % (which is disabled in R2014a)
    % Note: You cannot specify a larger number of workers in your pool than
    % what you have available.  I have a Dual Core system, so I cannot
    % specify more than 4 workers or my code will fail.

    
    % We will also wrap the matlabpool command to demonstrate how long it
    % can take to open the pool
    tic;
    matlabpool open 4;
    toc;

    tic;
    a=zeros(1000,10);        

    parfor m=1:1000
        for n=1:10
            a(m,n)=m*(m+1)*(n-1);
        end
        b=primes(a(m,n));
    end
    
    % Parfor loops always start from scratch distributing data to the
    % workers.  If the parfor loop is on the inside loop instead, this
    % means the data gets broadcasted out every time the for loop runs
    % another iteration.  Can generate a lot of overhead.
    % 
    
    % Display the time elapsed since tic was executed
    toc;
    
    % Close the matlabpool
    matlabpool close;
    
%% Notes

% It takes ~30 seconds to run the code in serial
% It takes ~8 seconds to open the pool of workers
% It takes ~11 seconds to execute the parfor commands

% You don't need to specify matlabpool to execute statements in parallel.
% In this instance, it slowed down our code.  However, if you do not want
% to use the defaults you need to utilize this command.  The default is to
% use one worker per core

