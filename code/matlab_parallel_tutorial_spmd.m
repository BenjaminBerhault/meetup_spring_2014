 %% matlab_parallel_tutorial_spmd.m
% Written by:   Shelley Knuth (shelley.knuth@colorado.edu)
% Affiliation:  Research Computing, CU-Boulder
% Date:         24 March 2014
% Purpose:      The purpose of this program is to demonstrate how to take
% normal Matlab code and convert it to run in parallel.


%% Now let's use the spmd command


    matlabpool open 4;

    spmd
        tic;
        c=zeros(1000,10);        

        for j=labindex:numlabs:1000
            %labindex is assigned to each worker when a job begins execution,
            %and applies only for the duration of that job. The value of labindex
            %spans from 1 to n, where n is the number of workers running the current 
            %job, defined by numlabs.
            
            for k=1:10
                c(j,k)=j*(j+1)*(k-1);
            end
            d=primes(c(j,k));
        end
        toc;
    end
    
    primes1=d{1};  % Set this variable to be one of the Composite objects so we can access it after pool closes
    
    matlabpool close;        
   