# Minecraft

## Write-up

extract the embedded png file using binwalk. 
we find that the CRC of the header for that file is broken , after analyzing the header we find that the CRC value is set to 0x00000000.  
calculate the crc , you'll find 0xe8d3c143. 
all that's left is replacing this correct crc value in file using a hex editor like hexedit
 
## Flag

`nexus{goTT4_RuN_Fr0M_crE3P3r$}`
