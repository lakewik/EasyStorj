<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Register</class>
 <widget class="QDialog" name="Register">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>394</width>
    <height>517</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Register account in Storj Network - Storj GUI Client</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>10</y>
     <width>371</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:16pt; font-weight:600;&quot;&gt;Register account in Storj Network&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>80</y>
     <width>101</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Bridge URL:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="Line" name="line">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>50</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="QLineEdit" name="bridge_url">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>70</y>
     <width>231</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>http://api.storj.io</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>220</y>
     <width>101</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Password:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="password">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>250</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLineEdit" name="password_2">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>340</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>310</y>
     <width>151</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Repeat password:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="email">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>170</y>
     <width>311</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="label_5">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>140</y>
     <width>101</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;E-mail:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="Line" name="line_2">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>110</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="QPushButton" name="register_bt">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>400</y>
     <width>361</width>
     <height>61</height>
    </rect>
   </property>
   <property name="text">
    <string>Register!</string>
   </property>
  </widget>
  <widget class="QPushButton" name="cancel_bt">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>470</y>
     <width>361</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Cancel</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
