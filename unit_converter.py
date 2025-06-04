def convert(value,From_unit,To_unit):
   factor={
      "mm":.001,
      "cm":.01,
      "m":1,
      "km":1000,
      "dm":.1,
      "ft":.3048,
      "in":.0254,
      "mile":1609.34

   }
   metres=value*factor[From_unit]
   result=metres/factor[To_unit]
   return result


print("WELCOME TO LENGTH UNIT CONVERTER")
print("\n")
From_unit=input("Enter 'FROM' unit:") 
To_unit=input("Enter 'TO' unit :")
value=float(input('Enter the value : '))
result=convert(value,From_unit,To_unit)
print("Converting {} {} into {}...".format(value,From_unit,To_unit))

print("Your result is : ",result,To_unit)
