#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on August 13, 2021, at 15:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'MET'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\PhD\\Dopa-HD\\MET - Practice\\MET_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instructions_text = visual.TextStim(win=win, name='Instructions_text',
    text='Welcome\nEmotiont reconition task - press corresponding number on keybord \nEmpthy - mouse click answere on slider and continue with space \n Space to start',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "EmRtrial"
EmRtrialClock = core.Clock()
Emo_image = visual.ImageStim(
    win=win,
    name='Emo_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Em_key_resp = keyboard.Keyboard()
Em_first_text = visual.TextStim(win=win, name='Em_first_text',
    text='default text',
    font='Arial',
    pos=(-0.5, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Em_second_text = visual.TextStim(win=win, name='Em_second_text',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Em_third_text = visual.TextStim(win=win, name='Em_third_text',
    text='default text',
    font='Arial',
    pos=(0.2, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Em_fourth_text = visual.TextStim(win=win, name='Em_fourth_text',
    text='default text',
    font='Arial',
    pos=(0.5, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Break_Emo"
Break_EmoClock = core.Clock()
Emo_break_text = visual.TextStim(win=win, name='Emo_break_text',
    text='Break \nSpace to continue',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
EmoBreak_key_resp = keyboard.Keyboard()

# Initialize components for Routine "EmpathyTrial"
EmpathyTrialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
EmpathyQ = visual.TextStim(win=win, name='EmpathyQ',
    text='How much do you emphasize with this person?',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Empathy_slider = visual.Slider(win=win, name='Empathy_slider',
    size=(1, 0.05), pos=(0, -0.35), units=None,
    labels=(1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
Empa_Next_key_resp = keyboard.Keyboard()
EmpInfo_text = visual.TextStim(win=win, name='EmpInfo_text',
    text='(Mouse click to select response and press space to continue)',
    font='Arial',
    pos=(0, -0.47), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Break_Emp"
Break_EmpClock = core.Clock()
Break_Emp_text = visual.TextStim(win=win, name='Break_Emp_text',
    text='Break \nSpace to continue ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break_key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
Thanks_text = visual.TextStim(win=win, name='Thanks_text',
    text='Thank You!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
Instructions_resp.keys = []
Instructions_resp.rt = []
_Instructions_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Instructions_text, Instructions_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_text* updates
    if Instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_text.frameNStart = frameN  # exact frame index
        Instructions_text.tStart = t  # local t and not account for scr refresh
        Instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_text, 'tStartRefresh')  # time at next scr refresh
        Instructions_text.setAutoDraw(True)
    
    # *Instructions_resp* updates
    waitOnFlip = False
    if Instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_resp.frameNStart = frameN  # exact frame index
        Instructions_resp.tStart = t  # local t and not account for scr refresh
        Instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_resp, 'tStartRefresh')  # time at next scr refresh
        Instructions_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructions_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructions_resp.status == STARTED and not waitOnFlip:
        theseKeys = Instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _Instructions_resp_allKeys.extend(theseKeys)
        if len(_Instructions_resp_allKeys):
            Instructions_resp.keys = _Instructions_resp_allKeys[-1].name  # just the last key pressed
            Instructions_resp.rt = _Instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_text.started', Instructions_text.tStartRefresh)
thisExp.addData('Instructions_text.stopped', Instructions_text.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Emo_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main_condition_Emo.xlsx'),
    seed=None, name='Emo_trials')
thisExp.addLoop(Emo_trials)  # add the loop to the experiment
thisEmo_trial = Emo_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmo_trial.rgb)
if thisEmo_trial != None:
    for paramName in thisEmo_trial:
        exec('{} = thisEmo_trial[paramName]'.format(paramName))

for thisEmo_trial in Emo_trials:
    currentLoop = Emo_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEmo_trial.rgb)
    if thisEmo_trial != None:
        for paramName in thisEmo_trial:
            exec('{} = thisEmo_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EmRtrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Emo_image.setImage(Main_images)
    Em_key_resp.keys = []
    Em_key_resp.rt = []
    _Em_key_resp_allKeys = []
    Em_first_text.setText(Em_first
)
    Em_second_text.setText(Em_second
)
    Em_third_text.setText(Em_third
)
    Em_fourth_text.setText(Em_fourth

)
    # keep track of which components have finished
    EmRtrialComponents = [Emo_image, Em_key_resp, Em_first_text, Em_second_text, Em_third_text, Em_fourth_text]
    for thisComponent in EmRtrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EmRtrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EmRtrial"-------
    while continueRoutine:
        # get current time
        t = EmRtrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EmRtrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emo_image* updates
        if Emo_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emo_image.frameNStart = frameN  # exact frame index
            Emo_image.tStart = t  # local t and not account for scr refresh
            Emo_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emo_image, 'tStartRefresh')  # time at next scr refresh
            Emo_image.setAutoDraw(True)
        
        # *Em_key_resp* updates
        waitOnFlip = False
        if Em_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Em_key_resp.frameNStart = frameN  # exact frame index
            Em_key_resp.tStart = t  # local t and not account for scr refresh
            Em_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Em_key_resp, 'tStartRefresh')  # time at next scr refresh
            Em_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Em_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Em_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Em_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Em_key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _Em_key_resp_allKeys.extend(theseKeys)
            if len(_Em_key_resp_allKeys):
                Em_key_resp.keys = _Em_key_resp_allKeys[-1].name  # just the last key pressed
                Em_key_resp.rt = _Em_key_resp_allKeys[-1].rt
                # was this correct?
                if (Em_key_resp.keys == str(Correct_buttonpress)) or (Em_key_resp.keys == Correct_buttonpress):
                    Em_key_resp.corr = 1
                else:
                    Em_key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Em_first_text* updates
        if Em_first_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Em_first_text.frameNStart = frameN  # exact frame index
            Em_first_text.tStart = t  # local t and not account for scr refresh
            Em_first_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Em_first_text, 'tStartRefresh')  # time at next scr refresh
            Em_first_text.setAutoDraw(True)
        
        # *Em_second_text* updates
        if Em_second_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Em_second_text.frameNStart = frameN  # exact frame index
            Em_second_text.tStart = t  # local t and not account for scr refresh
            Em_second_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Em_second_text, 'tStartRefresh')  # time at next scr refresh
            Em_second_text.setAutoDraw(True)
        
        # *Em_third_text* updates
        if Em_third_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Em_third_text.frameNStart = frameN  # exact frame index
            Em_third_text.tStart = t  # local t and not account for scr refresh
            Em_third_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Em_third_text, 'tStartRefresh')  # time at next scr refresh
            Em_third_text.setAutoDraw(True)
        
        # *Em_fourth_text* updates
        if Em_fourth_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Em_fourth_text.frameNStart = frameN  # exact frame index
            Em_fourth_text.tStart = t  # local t and not account for scr refresh
            Em_fourth_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Em_fourth_text, 'tStartRefresh')  # time at next scr refresh
            Em_fourth_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmRtrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EmRtrial"-------
    for thisComponent in EmRtrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Emo_trials.addData('Emo_image.started', Emo_image.tStartRefresh)
    Emo_trials.addData('Emo_image.stopped', Emo_image.tStopRefresh)
    # check responses
    if Em_key_resp.keys in ['', [], None]:  # No response was made
        Em_key_resp.keys = None
        # was no response the correct answer?!
        if str(Correct_buttonpress).lower() == 'none':
           Em_key_resp.corr = 1;  # correct non-response
        else:
           Em_key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Emo_trials (TrialHandler)
    Emo_trials.addData('Em_key_resp.keys',Em_key_resp.keys)
    Emo_trials.addData('Em_key_resp.corr', Em_key_resp.corr)
    if Em_key_resp.keys != None:  # we had a response
        Emo_trials.addData('Em_key_resp.rt', Em_key_resp.rt)
    Emo_trials.addData('Em_key_resp.started', Em_key_resp.tStartRefresh)
    Emo_trials.addData('Em_key_resp.stopped', Em_key_resp.tStopRefresh)
    Emo_trials.addData('Em_first_text.started', Em_first_text.tStartRefresh)
    Emo_trials.addData('Em_first_text.stopped', Em_first_text.tStopRefresh)
    Emo_trials.addData('Em_second_text.started', Em_second_text.tStartRefresh)
    Emo_trials.addData('Em_second_text.stopped', Em_second_text.tStopRefresh)
    Emo_trials.addData('Em_third_text.started', Em_third_text.tStartRefresh)
    Emo_trials.addData('Em_third_text.stopped', Em_third_text.tStopRefresh)
    Emo_trials.addData('Em_fourth_text.started', Em_fourth_text.tStartRefresh)
    Emo_trials.addData('Em_fourth_text.stopped', Em_fourth_text.tStopRefresh)
    # the Routine "EmRtrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break_Emo"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Emo_trials.thisN == 0 or Emo_trials.thisN % 10 != 0:
        continueRoutine = False
    EmoBreak_key_resp.keys = []
    EmoBreak_key_resp.rt = []
    _EmoBreak_key_resp_allKeys = []
    # keep track of which components have finished
    Break_EmoComponents = [Emo_break_text, EmoBreak_key_resp]
    for thisComponent in Break_EmoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Break_EmoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Break_Emo"-------
    while continueRoutine:
        # get current time
        t = Break_EmoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Break_EmoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Emo_break_text* updates
        if Emo_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Emo_break_text.frameNStart = frameN  # exact frame index
            Emo_break_text.tStart = t  # local t and not account for scr refresh
            Emo_break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Emo_break_text, 'tStartRefresh')  # time at next scr refresh
            Emo_break_text.setAutoDraw(True)
        
        # *EmoBreak_key_resp* updates
        waitOnFlip = False
        if EmoBreak_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EmoBreak_key_resp.frameNStart = frameN  # exact frame index
            EmoBreak_key_resp.tStart = t  # local t and not account for scr refresh
            EmoBreak_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EmoBreak_key_resp, 'tStartRefresh')  # time at next scr refresh
            EmoBreak_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EmoBreak_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EmoBreak_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EmoBreak_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = EmoBreak_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _EmoBreak_key_resp_allKeys.extend(theseKeys)
            if len(_EmoBreak_key_resp_allKeys):
                EmoBreak_key_resp.keys = _EmoBreak_key_resp_allKeys[-1].name  # just the last key pressed
                EmoBreak_key_resp.rt = _EmoBreak_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Break_EmoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break_Emo"-------
    for thisComponent in Break_EmoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Emo_trials.addData('Emo_break_text.started', Emo_break_text.tStartRefresh)
    Emo_trials.addData('Emo_break_text.stopped', Emo_break_text.tStopRefresh)
    # the Routine "Break_Emo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Emo_trials'


# set up handler to look after randomisation of conditions etc
Empa_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main_condition_Emo.xlsx'),
    seed=None, name='Empa_trials')
thisExp.addLoop(Empa_trials)  # add the loop to the experiment
thisEmpa_trial = Empa_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmpa_trial.rgb)
if thisEmpa_trial != None:
    for paramName in thisEmpa_trial:
        exec('{} = thisEmpa_trial[paramName]'.format(paramName))

for thisEmpa_trial in Empa_trials:
    currentLoop = Empa_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEmpa_trial.rgb)
    if thisEmpa_trial != None:
        for paramName in thisEmpa_trial:
            exec('{} = thisEmpa_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EmpathyTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Main_images)
    Empathy_slider.reset()
    Empa_Next_key_resp.keys = []
    Empa_Next_key_resp.rt = []
    _Empa_Next_key_resp_allKeys = []
    # keep track of which components have finished
    EmpathyTrialComponents = [image, EmpathyQ, Empathy_slider, Empa_Next_key_resp, EmpInfo_text]
    for thisComponent in EmpathyTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EmpathyTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EmpathyTrial"-------
    while continueRoutine:
        # get current time
        t = EmpathyTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EmpathyTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if Empathy_slider.getRating() != None:
              if 'space' in Empa_Next_key_resp.keys:
                  continueRoutine=False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *EmpathyQ* updates
        if EmpathyQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EmpathyQ.frameNStart = frameN  # exact frame index
            EmpathyQ.tStart = t  # local t and not account for scr refresh
            EmpathyQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EmpathyQ, 'tStartRefresh')  # time at next scr refresh
            EmpathyQ.setAutoDraw(True)
        
        # *Empathy_slider* updates
        if Empathy_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Empathy_slider.frameNStart = frameN  # exact frame index
            Empathy_slider.tStart = t  # local t and not account for scr refresh
            Empathy_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Empathy_slider, 'tStartRefresh')  # time at next scr refresh
            Empathy_slider.setAutoDraw(True)
        
        # *Empa_Next_key_resp* updates
        waitOnFlip = False
        if Empa_Next_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Empa_Next_key_resp.frameNStart = frameN  # exact frame index
            Empa_Next_key_resp.tStart = t  # local t and not account for scr refresh
            Empa_Next_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Empa_Next_key_resp, 'tStartRefresh')  # time at next scr refresh
            Empa_Next_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Empa_Next_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Empa_Next_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Empa_Next_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Empa_Next_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _Empa_Next_key_resp_allKeys.extend(theseKeys)
            if len(_Empa_Next_key_resp_allKeys):
                Empa_Next_key_resp.keys = _Empa_Next_key_resp_allKeys[-1].name  # just the last key pressed
                Empa_Next_key_resp.rt = _Empa_Next_key_resp_allKeys[-1].rt
        
        # *EmpInfo_text* updates
        if EmpInfo_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EmpInfo_text.frameNStart = frameN  # exact frame index
            EmpInfo_text.tStart = t  # local t and not account for scr refresh
            EmpInfo_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EmpInfo_text, 'tStartRefresh')  # time at next scr refresh
            EmpInfo_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmpathyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EmpathyTrial"-------
    for thisComponent in EmpathyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Empa_trials.addData('image.started', image.tStartRefresh)
    Empa_trials.addData('image.stopped', image.tStopRefresh)
    Empa_trials.addData('EmpathyQ.started', EmpathyQ.tStartRefresh)
    Empa_trials.addData('EmpathyQ.stopped', EmpathyQ.tStopRefresh)
    Empa_trials.addData('Empathy_slider.response', Empathy_slider.getRating())
    Empa_trials.addData('Empathy_slider.rt', Empathy_slider.getRT())
    Empa_trials.addData('Empathy_slider.started', Empathy_slider.tStartRefresh)
    Empa_trials.addData('Empathy_slider.stopped', Empathy_slider.tStopRefresh)
    Empa_trials.addData('EmpInfo_text.started', EmpInfo_text.tStartRefresh)
    Empa_trials.addData('EmpInfo_text.stopped', EmpInfo_text.tStopRefresh)
    # the Routine "EmpathyTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break_Emp"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Empa_trials.thisN == 0 or Empa_trials.thisN % 10 !=0:
        continueRoutine = False
    break_key_resp_2.keys = []
    break_key_resp_2.rt = []
    _break_key_resp_2_allKeys = []
    # keep track of which components have finished
    Break_EmpComponents = [Break_Emp_text, break_key_resp_2]
    for thisComponent in Break_EmpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Break_EmpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Break_Emp"-------
    while continueRoutine:
        # get current time
        t = Break_EmpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Break_EmpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_Emp_text* updates
        if Break_Emp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_Emp_text.frameNStart = frameN  # exact frame index
            Break_Emp_text.tStart = t  # local t and not account for scr refresh
            Break_Emp_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_Emp_text, 'tStartRefresh')  # time at next scr refresh
            Break_Emp_text.setAutoDraw(True)
        
        # *break_key_resp_2* updates
        waitOnFlip = False
        if break_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key_resp_2.frameNStart = frameN  # exact frame index
            break_key_resp_2.tStart = t  # local t and not account for scr refresh
            break_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key_resp_2, 'tStartRefresh')  # time at next scr refresh
            break_key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = break_key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _break_key_resp_2_allKeys.extend(theseKeys)
            if len(_break_key_resp_2_allKeys):
                break_key_resp_2.keys = _break_key_resp_2_allKeys[-1].name  # just the last key pressed
                break_key_resp_2.rt = _break_key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Break_EmpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break_Emp"-------
    for thisComponent in Break_EmpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Empa_trials.addData('Break_Emp_text.started', Break_Emp_text.tStartRefresh)
    Empa_trials.addData('Break_Emp_text.stopped', Break_Emp_text.tStopRefresh)
    # the Routine "Break_Emp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Empa_trials'


# ------Prepare to start Routine "Thanks"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [Thanks_text]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks_text* updates
    if Thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thanks_text.frameNStart = frameN  # exact frame index
        Thanks_text.tStart = t  # local t and not account for scr refresh
        Thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thanks_text, 'tStartRefresh')  # time at next scr refresh
        Thanks_text.setAutoDraw(True)
    if Thanks_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thanks_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Thanks_text.tStop = t  # not accounting for scr refresh
            Thanks_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Thanks_text, 'tStopRefresh')  # time at next scr refresh
            Thanks_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thanks_text.started', Thanks_text.tStartRefresh)
thisExp.addData('Thanks_text.stopped', Thanks_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
