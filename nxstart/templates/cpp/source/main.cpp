/**
 *  @file    main.cpp
 *  @author  APP_AUTHOR_PLACEHOLDER
 *  @date    DATE_PLACEHOLDER
 *  @version 1.0
 *
 *  This is the main file for APP_NAME_PLACEHOLDER.
 *
 */

#include <switch.h>								//The nxlib header file. It includes the functions which allow you to talk to the switch software/hardware
#include <stdio.h>								//Used for printf

int main(int argc, char** argv) {				//The main entry point
  u32 kdown = 0x00000000;						//We save the current button press state in there.
	
  socketInitializeDefault();					//Sets up the network sockets for nxlink
  nxlinkStdio();								//Sets up printf to be passed to our nxlink server on the computer

  consoleInit(nullptr);							//Setup the console
 
  while(appletMainLoop()) {						//Our main loop. As long as the program shouldn't close, keep executing our code
    hidScanInput();								//Scans our controllers for any button presses since the last time this function was called
    kdown = hidKeysDown(CONTROLLER_P1_AUTO);	//Read the last button presses and store them in the kdown variable. CONTROLLER_P1_AUTO reads the values from the currently used controller.
	
	//YOUR CODE GOES HERE
	
    if(kdown & KEY_PLUS)						//This isn't a convention but just for consistency. If the Plus button gets pressed, close the program. Most homebrews do that.
      break;
  }

  socketExit();									//Clean up after we're done and close our sockets.

  return 0;										//Terminate SUCCESSFULLY
}
