/**
 *  @file    main.cpp
 *  @author  APP_AUTHOR_PLACEHOLDER
 *  @date    DATE_PLACEHOLDER
 *  @version 0.0.1
 *
 *  This is the main file for APP_NAME_PLACEHOLDER.
 *  Original example file by WerWolv.
 */

#include <switch.h>     //The nxlib header file. It includes the functions which allow you to talk to the switch software/hardware
#include <stdio.h>      //Used for printf

//The main entry point
int main(int argc, char **argv) {
    // We save the current button press state in there.
    u32 kdown = 0x00000000;

    // Sets up the network sockets for nxlink
    socketInitializeDefault();

    // Sets up printf to be passed to our nxlink server on the computer
    // nxlinkStdio();

    // Setup the console
    consoleInit(nullptr);

    // Our main loop. As long as the program shouldn't close, keep executing our code
    while (appletMainLoop()) {
        // Scans our controllers for any button presses since the last time this function was called
        hidScanInput();

        // Read the last button presses and store them in the kdown variable. CONTROLLER_P1_AUTO reads the values from
        // the currently used controller.
        kdown = hidKeysDown(CONTROLLER_P1_AUTO);

        // YOUR CODE GOES HERE

        // This isn't a convention but just for consistency. If the Plus button gets pressed, close the program.
        // Most homebrews do that.
        if (kdown & KEY_PLUS)
            break;
    }

    //Clean up after we're done and close our sockets.
    socketExit();

    //Terminate SUCCESSFULLY
    return 0;
}
