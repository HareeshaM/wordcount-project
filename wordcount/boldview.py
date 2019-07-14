from django.http import HttpResponse

def eggs(request):
    return HttpResponse(""" <html lang="en" dir="ltr">
   <head>
      <meta charset="utf-8">
      <title>Table Quiz!</title>
   </head>
   <body>
      <table border="1">
         <thead>
            <th>Country Name</th>
            <th>Country Flag</th>
            <th>GDP (Millions of USD)</th>
         </thead>
         <tr>
            <td>Unites States</td>
            <td><img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/190px-Flag_of_the_United_States.svg.png" alt=""></td>
            <td>18,561,930</td>
         </tr>
         <tr>
            <td>India</td>
            <td><img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/150px-Flag_of_India.svg.png" alt=""></td>
            <td>2,250,990</td>
         </tr>
         <tr>
            <td>United Kingdom</td>
            <td><img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/200px-Flag_of_the_United_Kingdom.svg.png" alt=""></td>
            <td>2,649,890</td>
         </tr>
      </table>
   </body>
</html> """)
