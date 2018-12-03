#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h> 
#include <dirent.h> 
#include <sys/stat.h>
#include <sys/types.h>

off_t fsize(const char *filename) {
    struct stat st; 

    if (stat(filename, &st) == 0)
        return st.st_size;

    return -1; 
}
char * permissionBits(const char *filename) {
    struct stat ret; 
    char permission[9];
    if (stat(filename, &ret) == 0){
        int per = (ret.st_mode & S_IRUSR)|(ret.st_mode & S_IWUSR)|(ret.st_mode & S_IXUSR)|
        (ret.st_mode & S_IRGRP)|(ret.st_mode & S_IWGRP)|(ret.st_mode & S_IXGRP)|
        (ret.st_mode & S_IROTH)|(ret.st_mode & S_IWOTH)|(ret.st_mode & S_IXOTH);
    }
        int fileMode = ret.st_mode;
        int i = 0;

        /* Check owner permissions */
        if ((fileMode & S_IRUSR) && (fileMode & S_IREAD)){
            permission[i] = 'r';
            i++;
        }
        else
        {  
            permission[i] = '-';
            i++;
        }

        if ((fileMode & S_IWUSR) && (fileMode & S_IWRITE)){
            permission[i] = 'w';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }

        if ((fileMode & S_IXUSR) && (fileMode & S_IEXEC))
        {            
            permission[i] = 'x';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }

        /* Check group permissions */
        if ((fileMode & S_IRGRP) && (fileMode & S_IREAD))
          {            permission[i] = 'r';
            i++;}
        else{
            permission[i] = '-';
            i++;        
        }
        if ((fileMode & S_IWGRP) && (fileMode & S_IWRITE))
        {   permission[i] = 'w';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }

        if ((fileMode & S_IXGRP) && (fileMode & S_IEXEC))
        {  permission[i] = 'x';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }
        /* check other user permissions */
        if ((fileMode & S_IROTH) && (fileMode & S_IREAD))
        {   permission[i] = 'r';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }

        if ((fileMode & S_IWOTH) && (fileMode & S_IWRITE)){
            permission[i] = 'w';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }

        if ((fileMode & S_IXOTH) && (fileMode & S_IEXEC))
        {  /* because this is the last permission, leave 3 blank spaces after print */
            permission[i] = 'x';
            i++;
        }
        else{
            permission[i] = '-';
            i++;        
        }
        return permission;
}
struct FileDetails {
    unsigned long size;
    char permissionBit[9];
    char * fileName;

};

int main(int argc, char * const argv[])
{
    int opt;
    struct dirent *de;
    DIR *dir = opendir(".");
    bool sortByName = false, sortBySize = false, sortByDate = false;
    while ((opt = getopt(argc, argv, "ss:nd?")) != -1) {
        switch (opt) {
        case 's':
            sortBySize = true;
            // printf("%s", "Sorting by Size\n");
            break;
        case 'd':
            sortByDate = true;
            // printf("%s", "Sorting by Date\n");
            break;
        case 'n':
            sortByName = true;
            // printf("%s", "Sorting by Name\n");
            break;
        default:
            printf("%s","Unexpected argument, please change the argument value of the script\n");\
            return 0;
        }
    }
    int totalFiles = 0;
    
    while ((de = readdir(dir)) != NULL) {
        // char * fname = ();
        if( de->d_name[0] != '.' ){
            // printf("%lu %jd %s\n", de->d_ino, fsize(de->d_name), de->d_name);
            totalFiles++;
        }
    }
    closedir(dir);

    struct FileDetails allFiles[totalFiles];
    totalFiles = 0;
    dir = opendir(".");
    while ((de = readdir(dir)) != NULL) {
        // char * fname = ();
        if( de->d_name[0] != '.' ){
            // printf("%lu %jd %s\n", de->d_ino, fsize(de->d_name), de->d_name);
            struct FileDetails tmp;
            tmp.fileName = de->d_name;
            tmp.size = fsize(de->d_name);
            tmp.permissionBit = permissionBits(de);
            printf("%s\n", tmp.permissionBit);
            allFiles[totalFiles] = tmp;
            totalFiles++;
        }
    }
    for(int i=0;i<totalFiles;i++){
        permissionBits(allFiles[0].fileName);
        printf("%s\n", allFiles[i].fileName);
    }
    closedir(dir);

    return 0;
}
