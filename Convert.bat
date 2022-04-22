python Creat_hash_lookup.py "OneSeven Raw Texture Dumps" "Hash Look Up"
python Rename_Rexis_hashes_to_OneSeven_hashes.py "Hash Look Up" "Rexis Upscaled Textures" "Upscaled Mainline Textures (Output)"
python Find_files_missing_in_OneSeven_dump.py "Hash Look Up" "Rexis Upscaled Textures" "Need to dump"
python texture_dump_alpha_scaler.py unscale "Upscaled Mainline Textures (Output)" --force
