---
title: Robot Tank
---
# Robot Tank

```{figure} ../../_static/videos/atari/robotank.gif 
:width: 120px
:name: Robotank
```

This environment is part of the <a href='..'>Atari environments</a>. Please read that page first for general information.

|   |   |
|---|---|
| Action Space | Discrete(18) |
| Observation Space | (210, 160, 3) |
| Observation High | 255 |
| Observation Low | 0 |
| Import | `gym.make("ALE/Robotank-v0")` |

### Description
You control your Robot Tanks to destroy enemies and avoid enemy fire.

Game ends when all of your Robot Tanks are 
    destroyed or all 12 enemy squadrons are destroyed.

The game begins with one active Robot Tank and three reserves. 
Your Robot Tank may get lost when it is hit by enemy
    rocket fire - your video scrambles with _static interference when this
    happens - or just become damaged - sensors report the damage by flashing on your control panel (look at V/C/R/T squares).
    
You earn one bonus Robot Tank for every enemy squadron destroyed. The maximum
   number of bonus Robot Tanks allowed at any one time is 12.

Detailed documentation can be found on [the AtariAge page](https://atariage.com/manual_html_page.php?SoftwareLabelID=416)

### Actions
By default, all actions that can be performed on an Atari 2600 are available in this environment.Even if you use v0 or v4 or specify `full_action_space=False` during initialization, all actions will be available in the default flavor.

### Observations
By default, the environment returns the RGB image that is displayed to human players as an observation. However, it is
possible to observe
- The 128 Bytes of RAM of the console
- A grayscale image

instead. The respective observation spaces are
- `Box([0 ... 0], [255 ... 255], (128,), uint8)`
- `Box([[0 ... 0]
 ...
 [0  ... 0]], [[255 ... 255]
 ...
 [255  ... 255]], (250, 160), uint8)
`

respectively. The general article on Atari environments outlines different ways to instantiate corresponding environments
via `gym.make`.

### Rewards
The number of enemies destroyed is the only reward.

A small tank appears at the top of your screen for each enemy
   you destroy.  A square with the number 12 appears each time a squadron of twelve enemies are 
   destroyed.
   
For a more detailed documentation, see [the AtariAge page](https://atariage.com/manual_html_page.php?SoftwareLabelID=416).

### Arguments

```
env = gym.make("ALE/Robotank-v5")
```

The various ways to configure the environment are described in detail in the article on Atari environments.
It is possible to specify various flavors of the environment via the keyword arguments `difficulty` and `mode`. 
A flavor is a combination of a game mode and a difficulty setting.

|      Environment | Valid Modes                                                                                                                                                                         | Valid Difficulties | Default Mode |
|------------------|-------------------------|--------------------|--------------|
|             Robotank | `[0]`               |      `[0]` | `0`          |

You may use the suffix "-ram" to switch to the RAM observation space. In v0 and v4, the suffixes "Deterministic" and "NoFrameskip" 
are available. These are no longer supported in v5. In order to obtain equivalent behavior, pass keyword arguments to `gym.make` as outlined in 
the general article on Atari environments.
The versions v0 and v4 are not contained in the "ALE" namespace. I.e. they are instantiated via `gym.make("Robotank-v0")`.

### Version History
A thorough discussion of the intricate differences between the versions and configurations can be found in the
general article on Atari environments. 

* v5: Stickiness was added back and stochastic frameskipping was removed. The entire action space is used by default. The environments are now in the "ALE" namespace.
* v4: Stickiness of actions was removed
* v0: Initial versions release (1.0.0)
