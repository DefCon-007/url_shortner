# URL Shorner
A URL shortner made in django with CLI and file import features. 

# Building from source 
In terminal type the following commands.

- `git clone https://github.com/DefCon-007/url_shortner/`
- `cd url_shotner`
- `cp ./secrets-template.config ./secrets.config` 

- Now edit the `secrets.config` file and add all the required values.
- Create a virtual environement for the project using `virtualenv`. 
`pip install virtualenv`
`virtualenv -p python3 ./env`

- Activate the enviroment
`source ./env/bin/activate`
- Apply the django migrations (Use make migrations if you make changes to models.)
`python manage.py makemigrations`
`python manage.py migrate`

- Run the server.
`python manage.py runserver`
# Using the CLI 

After setting up the django project following the above steps, from the root directory use the following commands. 

###- Shortening a URL:

`python manage.py short --url <URL>` 

This will return the short URL for the given long URL with random key as in the following screenshot. 
<img width="646" alt="Screenshot 2020-02-09 at 9 48 53 PM" src="https://user-images.githubusercontent.com/16754547/74105690-27950580-4b86-11ea-90d1-a6c24cb8688f.png">

- Using custom shot name. 
Just add an argument `--name <SHORT_NAME>` to use a custom placeholder for the URL.

<img width="739" alt="Screenshot 2020-02-09 at 10 13 28 PM" src="https://user-images.githubusercontent.com/16754547/74106100-a93a6280-4b89-11ea-83a4-9cf9c0ff65ff.png">

 
###- Using a file as import: 

`python manage.py short --file <PATH_TO_FILE>`

This will return the the list of short URLs as output.

<img width="647" alt="Screenshot 2020-02-09 at 9 56 09 PM" src="https://user-images.githubusercontent.com/16754547/74105795-0254c700-4b87-11ea-8777-62925e406779.png">

For reference, below is the content of the test fiel used in above command.

```
http://www.google.com
http://www.google.com
http://www.google.com
http://www.google.com
http://www.google.com
http://www.google.com
```

###- Saving the output to a file: 

`python manage.py short --file <INPUT FILE PATH> --out <OUTPUT FILE PATH>`

Just add the flag `--out` with complete path of the output file and the previous command's output will be saved in the specified file.

<img width="836" alt="Screenshot 2020-02-09 at 10 01 19 PM" src="https://user-images.githubusercontent.com/16754547/74105899-d423b700-4b87-11ea-8f2c-b39473dfaaf5.png">


###- Using custom short names with file input:

Just separate the short name you like for the URL with a space in the file. 

<img width="634" alt="Screenshot 2020-02-09 at 10 04 37 PM" src="https://user-images.githubusercontent.com/16754547/74105953-498f8780-4b88-11ea-9962-d86600a5a9b0.png">


Below is the content of the file used in screenshot.
```
http://www.google.com fbbfe
http://www.google.com febefb
http://www.google.com 245
http://www.google.com lsn
http://www.google.com josfnbv
http://www.google.com jlfsn
```

