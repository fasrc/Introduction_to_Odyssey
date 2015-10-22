# Introduction to Odyssey Hands-on Exercises

## Login and Access
1. Using your terminal program, log into Odyssey
2. (optional) If you have XQuartz (Mac) or Xming (PC), Log into Odyssey w/ X11 forwarding. Start a GUI clock sessions with the command `xclock &`
3. (optional) Log on to one of our NX machines (`rcnx01` or `holynx01`) and start a terminal session


## Filesystems: Transferring files
**Transferring files with FileZilla**
  1. Download the file at https://github.com/fasrc/DataC-HPC-genomics/blob/master/data/genome_data.zip?raw=true to your desktop
  1. Using FileZilla transfer this file to your Odyssey account home/login folder
  2. On your laptop's Desktop, unzip the genome_data.zip archive
  2. Using Filezilla, transfer the genome_data folder over to your home folder on Odyssey

**(Mac/Linux) Transferring files with rsync**
`rsync` can transfer files within hosts or across hosts. The format is:
  
```
rsync (-options) source destination
rsync (-options) username@host:source destination
rsync (-options) source username@host:destination
```

where source and destination are any valid unix path

  1. In your terminal window from `Login and Access`, make a new directory 'transfer' in your home folder with the command `mkdir transfer`.
  2. Using your terminal program, transfer the zip archive from your Desktop to the `transfer` folder on Odyssey
  3. Using your terminal program, transfer the genome_data folder from your Desktop to the `transfer` folder on Odyssey


## Filesystems: Storage
1. See what directory you are in using `pwd` command. Compare this with your neighbor. Any differences?
2. You can display filesystems with the `df` command. Use this command with the following options:
  1. df /
  2. df .
  3. df -h .
3. What command would you use to see what other fileystems are available on Odyssey? ?


## Loading/installing software
1. Issue the command `bowtie`. What happens?
2. Issue the appropriate command to display what modules do you currently have loaded. What are they?
3. Using the appropriate command, find what versions of `bowtie` are on the cluster.
4. Load the latest version of bowtie. What command did you use?
5. What modules do you have loaded now?
6. Issue the `bowtie` command now. What's different?

7. Load in the legacy modules
8. Look for the versions of `bowtie` on the cluster again. What do you notice?

9. (Bonus!) Use the text editor `nano` to modify your `.bashrc` to opt-in for the new modules


## Login/Interactive sessions
1. Issue the appropriate command to get an interactive session w/ 4 GB RAM for 60 minutes
2. Start a MATLAB command-line session. What commands do you need to issue to do this?


## Submitting jobs
1. (single core) Using `nano` or your favorite text editor, create a SLURM submission script to run the `fastQTL` example code. We'll give you some biolerplate work...

```bash
source new-modules.sh
module load gcc FastQTL
cp -r $FASTQTL_HOME/example ./fastqtl_example
cd fastqtl_example
```

And execute `fastQTL` using the following parameters...

```bash
-V genotypes.vcf.gz
-B phenotypes.bed.gz 
-O file.results.gz 
-L file.log 
--include-covariates covariates.txt.gz 
--region 22:17517460-24322660
```

Also, include an email notification for END (at the least!) for yourself so that you know the status of your work.

2. Once your job completes successfully, how much RAM did your job use? What command did you use? Go back and modify your job script to use the appropriate amount of RAM.

3. (multicore) `FastQTL` can be parallelized easily using one of its options to create a command list. This command list can be passed to the program GNU Parallel `parallel`. Create a new submission script to process the `FastQTL` command list under `parallel` using 4 CPUs/cores. Ensure that you use the correct options for SLURM and `parallel` to specify this core count and the command list.

