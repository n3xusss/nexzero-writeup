# Write Up

    what you need to do is to unpack the binary using upx
    
    then after unpacking it it would become a normal binary written in go and all you need to do to dinamically analyse it or statically using you favorite tool and then you will see that it exits the program before executing the main function that prints the flag you can jump to it directly in gdb for example
or directly using dlv to debug go code
