#### Git for day to day usage

- open command prompt:$git --version #  check the version of git installed in your system

# system configuration 
we can apply it in 3 different levels
1. System level: All users of current computer
2. Global level: All repositories of the current user
3. Local level: The current repository

1. Name - $git config --global user.name "Pradeep"
2. Email - $git config --global user.email "k.b.v.pradeepkumar@gmail.com"
3. Default Editor - $git config --global core.editor "code --wait" # i am using vs code 
    $git config --global -e
4. Line Ending - $git config --global core.autocrlf true # for windows we have carriage return \r and line feed \n
               - $git config --global core.autocrlf input # for  mac and linux

# Git help
$git help  # all commands


# programing with mosh git course --> cheatsheet

staging area  - $git add . # add all files in the current directory
staging area  - $git add filename.txt # add a single file to the staging area







 




