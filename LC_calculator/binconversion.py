class Binary_conversion:
    
    def decimalToBinary(self,decimal): 
        """Converts a decimal number to binary and return the binary value.
        Args:
            decimal (int): The decimal number you want to convert
        Returns:
            binary (str): The binary result of the conversion
        full explanation:
        recursive function to convert a given decimal number into its binary representation. 
        It works by taking the remainder of the decimal number divided by two and appending it to a string(result),
        The remainder is then divided by two and the process repeats,
        until we reach zero. At which point the function returns the full binary result.
        """
        result= "" 
        # decimal = int(decimal)
        rem = decimal % 2  
        quotient = (decimal // 2)  
        if quotient > 0:  
            result = self.decimalToBinary(quotient)  
            result += str(rem) 
        else:  
            result += str(rem)   
        return result

    def binaryToDecimal(self,binary):
        decimal=0
        for i in range(len(binary)):
            dec= binary[len(binary)-i-1] 
            decimal+= int(dec)* pow(2,i)     
        return decimal
    