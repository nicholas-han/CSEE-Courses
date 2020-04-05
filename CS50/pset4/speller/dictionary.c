// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a trie
node *root;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        // if there is no memory allocated
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; ++i)
    {
        // initialize an array of null pointers
        root->children[i] = NULL;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        node *curNode = root;
        for (int i = 0; i < LENGTH + 1; ++i)
        {
            // break if this word is finished
            if (word[i] == '\0')
            {
                break;
            }

            int index = findIndex(word[i]);
            // if the specific child node points to null
            if (curNode->children[index] == NULL)
            {
                // create a node for this child to point to
                curNode->children[index] = malloc(sizeof(node));
                if (curNode->children[index] == NULL)
                {
                    // no memory allocated
                    return false;
                }
                curNode->children[index]->is_word = false;
                for (int j = 0; j < N; ++j)
                {
                    // initialize an array of null pointers
                    curNode->children[index]->children[j] = NULL;
                }
            }
            curNode = curNode->children[index];
        }
        curNode->is_word = true;

    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return sizeNode(root);

}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    node *curNode = root;
    for (int i = 0; word[i] != '\0'; ++i)
    {
        int index = findIndex(word[i]);
        // if char not found
        if (curNode->children[index] == NULL)
        {
            return false;
        }
        curNode = curNode->children[index];
    }
    if (curNode->is_word)
    {
        return true;
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    return unloadNode(root);
}

// find index for char
int findIndex(const char c)
{
    if (c >= 'a' && c <= 'z')
    {
        return c - 'a';
    }
    else if (c >= 'A' && c <= 'Z')
    {
        return c - 'A';
    }
    else if (c == '\'')
    {
        return N - 1;
    }
    else
    {
        return -1;
    }
}

// unload recursion
bool unloadNode(node *myNode)
{
    if (myNode != NULL)
    {
        for (int i = 0; i < N; ++i)
        {
            unloadNode(myNode->children[i]);
        }
        free(myNode);
    }
    return true;

}

// size recursion
int sizeNode(node *myNode)
{
    if (myNode == NULL)
    {
        return 0;
    }

    int counter = myNode->is_word;
    for (int i = 0; i < N; ++i)
    {
        counter += sizeNode(myNode->children[i]);
    }
    return counter;
}
