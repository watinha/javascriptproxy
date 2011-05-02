Author: Willian Massami Watanabe
contact info: talk@watinha.com
author webpage: http://watinha.com
twitter: @watinha
last updated: 02/03/2011

Introduction
============

This is the Javascript Proxy application. This application aims at providing a simple environment that lets you include javascripts directly into any webpage available on the web.

The Javascript Proxy application simply runs as a cross domain proxy design patterns, serving as a middle server of web applications. And while doing that, the application inserts javascripts and css stylesheets in the web application available. 

The application tries to provide a way of customizing the interaction and layout of applications as a test enviroment for usability experiments.

Howto use
=========

The JavaScript proxy application is executed in the Google AppEngine platform. As you run it you simply go for its url and give it a get parameter called url. This get parameter is supposed to contain the URL which you want to act as a proxy for. The idea is to be able to change the website from within and add new functionality to it, while keeping the DESIGN and Layout of the original website. 

Goal
====

The Goal of this application is to provide users with a good mock application for trying out new designs and javascript functionalities, while taking advantage of the original website layout and visual design.

By doing that we can conduct usability experiments to verify if the design and functionality changes actually improved the user experience for the web application.

Current Status
==============

Currently, the application simply copy the design of the web application and presents it for the user. The idea is to extend that to be abble to insert Scripts and Stylesheets on the fly for current available applications.

