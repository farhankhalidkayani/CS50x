#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check if there are two arguments
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open the memory card file
    FILE *file = fopen(argv[1], "r");

    // Check if the file can be opened
    if (file == NULL)
    {
        fprintf(stderr, "Invalid file\n");
        return 1;
    }

    int jpg_counter = 0;
    BYTE buffer[512];
    char filename[8];
    FILE *img = NULL;

    // Read the file block by block
    while (fread(&buffer, sizeof(buffer), 1, file))
    {
        // Check if the block is the start of a JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous image file if one is open
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new image file
            sprintf(filename, "%03i.jpg", jpg_counter);
            img = fopen(filename, "w");

            // Check if the new image file can be created
            if (img == NULL)
            {
                fprintf(stderr, "Could not create image file\n");
                fclose(file);
                return 1;
            }

            // Write the current block to the new image file
            fwrite(&buffer, sizeof(buffer), 1, img);

            // Increment the JPEG counter
            jpg_counter++;
        }
        else
        {
            // Continue writing to the current image file if one is open
            if (img != NULL)
            {
                fwrite(&buffer, sizeof(buffer), 1, img);
            }
        }
    }

    // Close the memory card file and the last image file
    fclose(file);
    if (img != NULL)
    {
        fclose(img);
    }

    return 0;
}