#!/usr/bin/env python
# //==============================================================================
# /*
#     Software License Agreement (BSD License)
#     Copyright (c) 2020, AIMGaitCore
#     (www.aimlab.wpi.edu)

#     All rights reserved.

#     Redistribution and use in source and binary forms, with or without
#     modification, are permitted provided that the following conditions
#     are met:

#     * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.

#     * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.

#     * Neither the name of authors nor the names of its contributors may
#     be used to endorse or promote products derived from this software
#     without specific prior written permission.

#     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#     "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#     LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#     FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#     COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#     INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#     BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#     LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#     LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#     ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#     POSSIBILITY OF SUCH DAMAGE.

#     \author    <http://www.aimlab.wpi.edu>
#     \author    <nagoldfarb@wpi.edu>
#     \author    Nathaniel Goldfarb
#     \version   0.1
# */
# //==============================================================================




class Joint(object):
    """
    joint class
    """
    def __init__(self, angle, moment, power, force):
        """
        Holds the joint data form the model output
        :param angle: angles
        :param moment: moments
        :param power: power
        :param force: forces
        """

        self._angle = angle
        self._moment = moment
        self._power = power
        self._force = force

    @property
    def angle(self):
        """
        get the angles for the joint
        """
        return self._angle

    @property
    def power(self):
        """
        get the power of the joint
        """
        return self._power

    @property
    def force(self):
        """
        get the forces of the joint
        """
        return self._force

    @property
    def moment(self):
        """
        get the moment of the joint
        """
        return self._moment

    @angle.setter
    def angle(self, value):
        self._angle = value

    @power.setter
    def power(self, value):
        self._power = value

    @force.setter
    def force(self, value):
        self._force = value

    @moment.setter
    def moment(self, value ):
        self._moment = value

