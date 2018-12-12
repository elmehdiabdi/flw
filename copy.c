#include <stdio.h>
#include <sys/mman.h>
#include <stdio.h> 
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>




int main(int argc, char *argv[] ){
    printf("Starting File Copy...\n");
    int sfd, dfd;
    char *src, *dest;
    size_t filesize;

    // /* SOURCE */
    // printf("%i", argc);
    if(argc < 3){
        printf("%s", "Expected two arguments ./copy [source-file-path] [destination-filepath]\n");
        return 0;
    }
    char* source = argv[1];
    char* destination  = argv[2];
    printf("Copying from %s to %s \n", source, destination);
    sfd = open(source, O_RDONLY);
    filesize = lseek(sfd, 0, SEEK_END);

    src = mmap(NULL, filesize, PROT_READ, MAP_PRIVATE, sfd, 0);

    // /* DESTINATION */
    dfd = open(destination, O_RDWR | O_CREAT, 0666);

    ftruncate(dfd, filesize);

    dest = mmap(NULL, filesize, PROT_READ | PROT_WRITE, MAP_SHARED, dfd, 0);

    // /* COPY */

    memcpy(dest, src, filesize);

    munmap(src, filesize);
    munmap(dest, filesize);

    close(sfd);
    close(dfd);
    printf("Done\n");

    return 0;
}