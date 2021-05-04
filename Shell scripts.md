# Shell scripts

Replace all string in a file
[Reference](https://linuxhint.com/replace_string_in_file_bash/)

```
$ sed -i 's/search_string/replace_string/g' filename
```

Read from input

[Reference](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php)

`read.sh`
```
#!/bin/bash
# Ask the user for their name
echo Hello, who am I talking to?
read varname
echo It\'s nice to meet you $varname
```

Read parameters

[Reference](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script)


`read.sh`
```
#!/bin/bash
while getopts u:a:f: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        a) age=${OPTARG};;
        f) fullname=${OPTARG};;
    esac
done
echo "Username: $username";
echo "Age: $age";
echo "Full Name: $fullname";
```