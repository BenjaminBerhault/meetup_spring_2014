#PBS -l nodes=1:ppn=1,walltime=00:10:00
#PBS -N matlab_test_serial
#PBS -q janus-debug
#PBS -m be 
#PBS -M shelley.knuth@colorado.edu
#PBS -j oe

# Written by:	Shelley Knuth
# Date:		24 February 2014
# Purpose: 	This script is for the Matlab tutorial.  Its purpose is 
#		to demonstrate how to submit a serial Matlab job from a 
#		batch script on the Janus computers	


# load the matlab module
module load matlab/matlab-2012b

# The directory where the job was submitted from
cd $PROJECTS

# Run matlab without a GUI
# Insert Matlab code
# The << characters set up a heredoc that runs from the first EOF till it finds EOF again
matlab -nosplash -nodesktop << EOF
  var1=zeros(50,1);
for i=1:10
   var1(i)=var1(i)+var1(i)*ln(var1(i));
end

% Save all variables from the current workspace 
% Make sure you save the variables or else everything will be deleted at the end of the Matlab session
save test_var.mat  

% Make sure you exit Matlab!!
exit
EOF
