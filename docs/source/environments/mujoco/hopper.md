---
AUTOGENERATED: DO NOT EDIT FILE DIRECTLY
title: Hopper
---

# Hopper

```{figure} ../../_static/videos/mujoco/hopper.gif 
:width: 200px
:name: hopper
```

This environment is part of the <a href='..'>Mujoco environments</a>. Please read that page first for general information.

|   |   |
|---|---|
| Action Space | Box(-1.0, 1.0, (3,), float32) |
| Observation Shape | (11,) |
| Observation High | [inf inf inf inf inf inf inf inf inf inf inf] |
| Observation Low | [-inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf] |
| Import | `gym.make("Hopper-v3")` | 


### Description

This environment is based on the work done by Erez, Tassa, and Todorov in
["Infinite Horizon Model Predictive Control for Nonlinear Periodic Tasks"](http://www.roboticsproceedings.org/rss07/p10.pdf). The environment aims to
increase the number of independent state and control variables as compared to
the classic control environments. The hopper is a two-dimensional
one-legged figure that consist of four main body parts - the torso at the
top, the thigh in the middle, the leg in the bottom, and a single foot on
which the entire body rests. The goal is to make hops that move in the
forward (right) direction by applying torques on the three hinges
connecting the four body parts.

### Action Space
The action space is a `Box(-1, 1, (3,), float32)`. An action represents the torques applied between *links*

| Num | Action                             | Control Min | Control Max | Name (in corresponding XML file) | Joint | Unit         |
|-----|------------------------------------|-------------|-------------|----------------------------------|-------|--------------|
| 0   | Torque applied on the thigh rotor  | -1          | 1           | thigh_joint                      | hinge | torque (N m) |
| 1   | Torque applied on the leg rotor    | -1          | 1           | leg_joint                        | hinge | torque (N m) |
| 3   | Torque applied on the foot rotor   | -1          | 1           | foot_joint                       | hinge | torque (N m) |

### Observation Space

Observations consist of positional values of different body parts of the
hopper, followed by the velocities of those individual parts
(their derivatives) with all the positions ordered before all the velocities.

By default, observations do not include the x-coordinate of the hopper. It may
be included by passing `exclude_current_positions_from_observation=False` during construction.
In that case, the observation space will have 12 dimensions where the first dimension
represents the x-coordinate of the hopper.
Regardless of whether `exclude_current_positions_from_observation` was set to true or false, the x-coordinate
will be returned in `info` with key `"x_position"`.

However, by default, the observation is a `ndarray` with shape `(11,)` where the elements
correspond to the following:

| Num | Observation           | Min                  | Max                | Name (in corresponding XML file) | Joint| Unit |
|-----|-----------------------|----------------------|--------------------|----------------------|--------------------|--------------------|
| 0   | z-coordinate of the top (height of hopper)       | -Inf                 | Inf                | rootz | slide | position (m) |
| 1   | angle of the top                                 | -Inf                 | Inf                | rooty | hinge | angle (rad) |
| 2   | angle of the thigh joint                         | -Inf                 | Inf                | thigh_joint | hinge | angle (rad) |
| 3   | angle of the leg joint                           | -Inf                 | Inf                | leg_joint | hinge | angle (rad) |
| 4   | angle of the foot joint                          | -Inf                 | Inf                | foot_joint | hinge | angle (rad) |
| 5   | velocity of the x-coordinate of the top          | -Inf                 | Inf                | rootx | slide | velocity (m/s) |
| 6   | velocity of the z-coordinate (height) of the top | -Inf                 | Inf                | rootz | slide | velocity (m/s)  |
| 7   | angular velocity of the angle of the top         | -Inf                 | Inf                | rooty | hinge | angular velocity (rad/s) |
| 8   | angular velocity of the thigh hinge              | -Inf                 | Inf                | thigh_joint | hinge | angular velocity (rad/s) |
| 9   | angular velocity of the leg hinge                | -Inf                 | Inf                | leg_joint | hinge | angular velocity (rad/s) |
| 10  | angular velocity of the foot hinge               | -Inf                 | Inf                | foot_joint | hinge | angular velocity (rad/s) |

### Rewards
The reward consists of three parts:
- *healthy_reward*: Every timestep that the hopper is healthy (see definition in section "Episode Termination"), it gets a reward of fixed value `healthy_reward`.
- *forward_reward*: A reward of hopping forward which is measured
as *`forward_reward_weight` * (x-coordinate before action - x-coordinate after action)/dt*. *dt* is
the time between actions and is dependent on the frame_skip parameter
(fixed to 4), where the frametime is 0.002 - making the
default *dt = 4 * 0.002 = 0.008*. This reward would be positive if the hopper
hops forward (positive x direction).
- *ctrl_cost*: A cost for penalising the hopper if it takes
actions that are too large. It is measured as *`ctrl_cost_weight` *
sum(action<sup>2</sup>)* where *`ctrl_cost_weight`* is a parameter set for the
control and has a default value of 0.001

The total reward returned is ***reward*** *=* *healthy_reward + forward_reward - ctrl_cost* and `info` will also contain the individual reward terms

### Starting State
All observations start in state
(0.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) with a uniform noise
 in the range of [-`reset_noise_scale`, `reset_noise_scale`] added to the values for stochasticity.

### Episode Termination
The hopper is said to be unhealthy if any of the following happens:

1. An element of `observation[1:]` (if  `exclude_current_positions_from_observation=True`, else `observation[2:]`) is no longer contained in the closed interval specified by the argument `healthy_state_range`
2. The height of the hopper (`observation[0]` if  `exclude_current_positions_from_observation=True`, else `observation[1]`) is no longer contained in the closed interval specified by the argument `healthy_z_range` (usually meaning that it has fallen)
3. The angle (`observation[1]` if  `exclude_current_positions_from_observation=True`, else `observation[2]`) is no longer contained in the closed interval specified by the argument `healthy_angle_range`

If `terminate_when_unhealthy=True` is passed during construction (which is the default),
the episode terminates when any of the following happens:

1. The episode duration reaches a 1000 timesteps
2. The hopper is unhealthy

If `terminate_when_unhealthy=False` is passed, the episode is terminated only when 1000 timesteps are exceeded.

### Arguments

No additional arguments are currently supported in v2 and lower.

```
env = gym.make('Hopper-v2')
```

v3 and beyond take gym.make kwargs such as xml_file, ctrl_cost_weight, reset_noise_scale etc.

```
env = gym.make('Hopper-v3', ctrl_cost_weight=0.1, ....)
```

| Parameter               | Type       | Default        |Description                    |
|-------------------------|------------|----------------|-------------------------------|
| `xml_file`              | **str**    | `"hopper.xml"` | Path to a MuJoCo model |
| `forward_reward_weight` | **float**  | `1.0`          | Weight for *forward_reward* term (see section on reward) |
| `ctrl_cost_weight`      | **float**  | `0.001`        | Weight for *ctrl_cost* reward (see section on reward) |
| `healthy_reward`        | **float**  | `1`            | Constant reward given if the ant is "healthy" after timestep |
| `terminate_when_unhealthy` | **bool**| `True`         | If true, issue a done signal if the hopper is no longer healthy |
| `healthy_state_range`   | **tuple**  | `(-100, 100)`  | The elements of `observation[1:]` (if  `exclude_current_positions_from_observation=True`, else `observation[2:]`) must be in this range for the hopper to be considered healthy |
| `healthy_z_range`       | **tuple**  | `(0.7, float("inf"))`    | The z-coordinate must be in this range for the hopper to be considered healthy |
| `healthy_angle_range`   | **tuple**  | `(-0.2, 0.2)`   | The angle given by `observation[1]` (if  `exclude_current_positions_from_observation=True`, else `observation[2]`) must be in this range for the hopper to be considered healthy |
| `reset_noise_scale`     | **float**  | `5e-3`         | Scale of random perturbations of initial position and velocity (see section on Starting State) |
| `exclude_current_positions_from_observation`| **bool** | `True`| Whether or not to omit the x-coordinate from observations. Excluding the position can serve as an inductive bias to induce position-agnostic behavior in policies |


### Version History

* v3: support for gym.make kwargs such as xml_file, ctrl_cost_weight, reset_noise_scale etc. rgb rendering comes from tracking camera (so agent does not run away from screen)
* v2: All continuous control environments now use mujoco_py >= 1.50
* v1: max_time_steps raised to 1000 for robot based tasks. Added reward_threshold to environments.
* v0: Initial versions release (1.0.0)
