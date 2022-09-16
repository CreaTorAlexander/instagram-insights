const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
const cheerio = require("cheerio")
const puppeteer = require('puppeteer');
const jsdom = require('jsdom')
const dom = new jsdom.JSDOM("")
const jquery = require('jquery')(dom.window)





// URL to my own profile, but later on make it variable and controlled by the user
const URL = "https://www.instagram.com/aalexhess/followers/";
const FOLLOWER_ELEMENT = `<div style="style="position: relative; display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px;">`;
const FOLLOWER_ELEMENT_CLASS = `_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm`


// ._ab8y, div._ab94, div._ab97, div._ab9f, div._ab9k, div._ab9p, div._abcm
let span = "span._ac2a";
// let one_follower_element = $("span._ac2a");

// console.log(one_follower_element.children)


async function getFollowerCount() {
   const url = `https://www.instagram.com/aalexhess/`;
   console.log('Accessing site for follower count');
   puppeteer
     .launch()
     .then(function(browser) {
       return browser.newPage();
     })
     .then(function(page) {
       return page.goto(url).then(function() {
         return page.content();
       });
     })
     .then(function(html) {
       let arr = [];
       console.log('Scraping for follower count');
       console.log(document.getElementsByClassName('._ac2a'))

       followerCount = parseInt(arr[1].replace(',', ''));
       console.log(`Number of followers: ${followerCount}`);
     })
     .catch(function(err) {
       console.log(err);
     });
 }

 getFollowerCount()