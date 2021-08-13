#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on August 12, 2021, at 11:08
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
    originPath='E:\\PhD\\Dopa-HD\\MET\\MET.py',
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

# Initialize components for Routine "EmRtrial"
EmRtrialClock = core.Clock()
Emo_image = visual.ImageStim(
    win=win,
    name='Emo_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
Em_first_text = visual.TextStim(win=win, name='Em_first_text',
    text='default text',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
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
    pos=(0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Take a break press space to continue ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break_key_resp = keyboard.Keyboard()

# Initialize components for Routine "EmpathyTrial"
EmpathyTrialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
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

# Initialize components for Routine "Break_Emp"
Break_EmpClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Take a break press space to continue ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
break_key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main_condition_Emo.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EmRtrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Emo_image.setImage(Main_images)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    Em_first_text.setText(Em_first
)
    Em_second_text.setText(Em_second
)
    Em_third_text.setText(Em_third
)
    Em_fourth_text.setText(Em_fourth

)
    # keep track of which components have finished
    EmRtrialComponents = [Emo_image, key_resp, Em_first_text, Em_second_text, Em_third_text, Em_fourth_text]
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
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(Correct_buttonpress)) or (key_resp.keys == Correct_buttonpress):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
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
    trials.addData('Emo_image.started', Emo_image.tStartRefresh)
    trials.addData('Emo_image.stopped', Emo_image.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(Correct_buttonpress).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('Em_first_text.started', Em_first_text.tStartRefresh)
    trials.addData('Em_first_text.stopped', Em_first_text.tStopRefresh)
    trials.addData('Em_second_text.started', Em_second_text.tStartRefresh)
    trials.addData('Em_second_text.stopped', Em_second_text.tStopRefresh)
    trials.addData('Em_third_text.started', Em_third_text.tStartRefresh)
    trials.addData('Em_third_text.stopped', Em_third_text.tStopRefresh)
    trials.addData('Em_fourth_text.started', Em_fourth_text.tStartRefresh)
    trials.addData('Em_fourth_text.stopped', Em_fourth_text.tStopRefresh)
    # the Routine "EmRtrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trials.thisN == 0 or trials.thisN % 10 !=0:
        continueRoutine = False
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
    # keep track of which components have finished
    BreakComponents = [text, break_key_resp]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *break_key_resp* updates
        waitOnFlip = False
        if break_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key_resp.frameNStart = frameN  # exact frame index
            break_key_resp.tStart = t  # local t and not account for scr refresh
            break_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key_resp, 'tStartRefresh')  # time at next scr refresh
            break_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = break_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _break_key_resp_allKeys.extend(theseKeys)
            if len(_break_key_resp_allKeys):
                break_key_resp.keys = _break_key_resp_allKeys[-1].name  # just the last key pressed
                break_key_resp.rt = _break_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Main_condition_Emo.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EmpathyTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Main_images)
    Empathy_slider.reset()
    Empa_Next_key_resp.keys = []
    Empa_Next_key_resp.rt = []
    _Empa_Next_key_resp_allKeys = []
    # keep track of which components have finished
    EmpathyTrialComponents = [image, EmpathyQ, Empathy_slider, Empa_Next_key_resp]
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
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    trials_2.addData('EmpathyQ.started', EmpathyQ.tStartRefresh)
    trials_2.addData('EmpathyQ.stopped', EmpathyQ.tStopRefresh)
    trials_2.addData('Empathy_slider.response', Empathy_slider.getRating())
    trials_2.addData('Empathy_slider.rt', Empathy_slider.getRT())
    trials_2.addData('Empathy_slider.started', Empathy_slider.tStartRefresh)
    trials_2.addData('Empathy_slider.stopped', Empathy_slider.tStopRefresh)
    # the Routine "EmpathyTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break_Emp"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trials_2.thisN == 0 or trials_2.thisN % 10 !=0:
        continueRoutine = False
    break_key_resp_2.keys = []
    break_key_resp_2.rt = []
    _break_key_resp_2_allKeys = []
    # keep track of which components have finished
    Break_EmpComponents = [text_2, break_key_resp_2]
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
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
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
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "Break_Emp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


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
