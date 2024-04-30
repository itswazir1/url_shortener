import pyshorteners 
wzr="""
       $$$$              $$$$   $$$$$$$$$$   $$$$$$$$$$$     $$$$    $$$$$$$$$$$
       ####              ####   ###    ###          ###      ####    ####      ###
       %%%%              %%%%   %%%    %%%        %%%        %%%%    %%%%     %%%
       &&&&     ####     &&&&   &&&####&&&      &&&          &&&&    &&&&&&&&&&
       @@@@   $$$  $$$   @@@@   @@@    @@@    @@@            @@@@    @@@@     @@@
       !!!!@@@        @@@!!!!   !!!    !!!    !!!!!!!!!!!    !!!!    !!!!       !!!
       
       """
print(wzr)
url_str="""
   What type of URl You want . Select below URLS.

  1) Tiny_Url : Example : https://tinyurl.com/xyz
  2) Bitly_Url: Example : https://bit.ly/xyz 
    
  Note: URL must be Start from https://example.com
    """
print(url_str)
url_choice=int(input("  Enter Your options between 1 and 2 :)  "))
if url_choice==1:
    input_tiny_url=input("Enter Url Here! ")
    tiny_url=pyshorteners.Shortener()
    convert_url=tiny_url.tinyurl.short(input_tiny_url)
    print(f" New Url is : {convert_url}")
elif url_choice==2:
     input_bitly_url=input("Enter Url Here!")
     bitly_url=pyshorteners.Shortener(api_key='e8a728a156685d3b6efd1b9c1614f6dc5b41f13c')
     convert_bitly_url=bitly_url.bitly.short(input_bitly_url)
     print(f"New URl is : {convert_bitly_url}")
else:
     print(" You Entered invalid URl ")