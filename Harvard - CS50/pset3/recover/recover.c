#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t  BYTE;
typedef struct
{
    BYTE block;
} __attribute__((__packed__))
BLOCK;


int main(int argc, char *argv[])
{
    // check number of command line arguments
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // open input file
    char *fileName = argv[1];
    FILE *inptr = fopen(fileName, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Cannot open file.\n");
        return 2;
    }

    const int BLOCKSIZE = 512;
    BLOCK buffer[BLOCKSIZE];
    int fileCounter = 0;
    FILE *outptr = NULL;
    char jpegName[10];

    int counter = 0;
    while (fread(&buffer, sizeof(BLOCK), BLOCKSIZE, inptr) == BLOCKSIZE)
    {
        // if the beginning of a JPEG
        if (buffer[0].block == 0xff && buffer[1].block == 0xd8 && buffer[2].block == 0xff && (buffer[3].block & 0xf0) == 0xe0)
        {
            // if not first jpeg, close previous jpeg
            if (outptr)
            {
                fclose(outptr);
            }

            // create new jpeg
            sprintf(jpegName, "%03i.jpg", fileCounter);
            outptr = fopen(jpegName, "w");
            fwrite(&buffer, 1, sizeof(BLOCK) * BLOCKSIZE, outptr);

            fileCounter++;

        }

        // if not beginning but part of a jpeg
        else if (outptr)
        {
            fwrite(&buffer, 1, sizeof(BLOCK) * BLOCKSIZE, outptr);
        }
    }

    if (outptr)
    {
        fclose(outptr);
    }

}
