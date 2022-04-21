python Create_multi_hash_dumped_tex.py "OneSeven Raw Texture Dumps" "Multi Hash Raw Texture Dumps"
python Rename_Rexis_hashes_to_OneSeven_hashes.py "Multi Hash Raw Texture Dumps" "Rexis Replacement Textures" "OneSeven Replacement Textures" --doubleCheck
python Find_files_missing_in_OneSeven_dump.py "Multi Hash Raw Texture Dumps" "Rexis Replacement Textures" "Need to dump"
python texture_dump_alpha_scaler.py unscale "OneSeven Replacement Textures" --force
