* attach gdb to the chall process
* you will notice after some debuging the ascii values in edx
* print the ascii values using gdb script or the gdb python api
```

set logging enabled on
define f
    while(1)
         if $edx<255 && $edx>30
      	     printf"%c\n",$edx
     	     end
         ni
         end
    end

f
```
* parse the log file for the flag
