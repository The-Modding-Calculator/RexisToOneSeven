# RexisToOneSeven 
A set of scripts to convert textures intended for use with PCSX2-Rexis' texture replacement system to the main line PCSX2 texture replacement system, for use by the P3HD Overhaul Project 

# Quick Start 
1) dump as many textures in mainline PCSX2 as you can 
2) Run the Make directorys.bat this will create the directories used by convert.bat 
3) Copy the textures you dumped from PCSX2 to "OneSeven Raw Texture Dumps" 
4) Copy your PCSX2-Rexis replacement textures to "Rexis Replacement Textures" 
5) run convert.bat and make some tea (it takes a while) 
  

# Glossory because I'm bad at naming things 
One Seven = main line PCSX2 

Raw Dump = texture that's been dumped and not been modified 

Multi Hash = file names that contain both Rexis and mainline hashes separated by an under score 
  

# What each script does 
Create_multi_hash_dumped_tex: 
Copys dumped mainline PCSX2 textures to a new directory and add Rexis hashes to the start of the file name 
  

Rename_Rexis_hashes_to_OneSeven_hashes: 
Copys the replacement textures for Rexis to a new directory but gives them mainline PCSX2 hashes using textures in the multihash directory to look up the new hashes 
  

texture_dump_alpha_scaler: 
This is just a slightly modified script form the PCSX2 repo. It's used to half the alpha values of textures and I also made it convert textures to RGBA if they're not already 
  

# Todo 
replace Multi Hash Raw Texture Dumps with a txt file because using a directory instead as a look up table is ridiculous 
