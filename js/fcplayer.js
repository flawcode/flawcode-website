/*global $, document, alert*/

(function () {

  // Track multiple players on the page
  var fcplayers = [];


  // Stop all other fcplayers on page when starting another
  function stopAllfcPlayers() {
    var i = 0;
    for (i = 0; i < fcplayers.length; i++) {
      fcplayers[i].fcaudio.pause();
      fcplayers[i].updateDisplay();
    }
  }

  // Pad a number with leading zeros
  function zeroPad(number, places) {
    var zeros = places - number.toString().length + 1;
    return new Array(+(zeros > 0 && zeros)).join("0") + number;
  }


  // Convert seconds to mm:ss format
  function toTimeString(seconds) {
    if (isNaN(seconds)) {
      return "--:--";
    }
    var minutes = Math.floor(seconds / 60);
    seconds = seconds - minutes * 60;
    return zeroPad(minutes, 2) + ":" + zeroPad(seconds, 2);
  }


  // Parse out file name from path, unescape
  function parseTitle(path) {
    path = decodeURI(path);
    return path.split('/').pop().split('.').shift();
  }

  // Object to represent fcplayer
  var fcPlayer = function (elem) {
    this.fcplayer  = elem;
    this.fcaudio   = elem.getElementsByTagName("audio").item(0);
    this.fcdebug   = elem.getElementsByClassName("fc-debug").item(0);
    this.fcaudio.setAttribute("preload", "meta");
    this.state     = this.fcaudio.autoplay ? "playing" : "paused";
    this.repeat    = this.fcaudio.loop ? true : false;
    this.fcaudio.removeAttribute('loop'); // hijack the loop directive
    this.trackList = [];
    this.init();
  }


  // Debug logger
  fcPlayer.prototype.log = function (msg) {
    if (this.fcdebug) {
      this.fcdebug.appendChild(document.createTextNode(msg));
      this.fcdebug.appendChild(document.createElement('br'));
      this.fcdebug.scrollTop = (this.fcdebug.scrollHeight - this.fcdebug.clientHeight);
    }
  };


  // say if audio element can play file type
  fcPlayer.prototype.canPlay = function (extension) {
    if ((/mp3/i).test(extension) && this.fcaudio.canPlayType('audio/mpeg')) {
      return true;
    }
    if ((/ogg/i).test(extension) && this.fcaudio.canPlayType('audio/ogg')) {
      return true;
    }
    return false;
  };


  // Set up multiple sources as track list,
  // Remove duplicate and unplayable sources
  fcPlayer.prototype.loadSources = function () {
    var self = this;
    var unused = [];
    self.log('func: loadSources');
    var sources = self.fcaudio.getElementsByTagName("source");
    [].forEach.call(
      self.fcaudio.getElementsByTagName("source"),
      function (elem) {
        var fileName  = elem.getAttribute('src').split('/').pop();
        var extension = fileName.split('.').pop();
        var trackName = fileName.split('.').shift();
        var playable  = self.canPlay(extension);
        if (self.trackList.indexOf(trackName) === -1 && playable === true) {
          self.trackList.push(trackName);
        } else {
          unused.push(elem);
        }
      }
    );
    [].forEach.call(
      unused,
      function (elem) {
        elem.parentNode.removeChild(elem);
      }
    );
  };


  // Update display
  fcPlayer.prototype.updateDisplay = function () {
    var audioElem = this.fcaudio;
    var duration  = toTimeString(Math.ceil(audioElem.duration));
    var elapsed   = toTimeString(Math.ceil(audioElem.currentTime));
    var title     = parseTitle(audioElem.currentSrc);
    this.fcplayer.getElementsByClassName('fc-trackLength').item(0).innerHTML = duration;
    this.fcplayer.getElementsByClassName('fc-trackTime').item(0).innerHTML = elapsed;
    this.fcplayer.getElementsByClassName('fc-trackTitle').item(0).innerHTML = title;
    var playButton = this.fcplayer.getElementsByClassName("fc-play").item(0);
    if (this.fcaudio.paused) {
      playButton.classList.remove("fc-playing");
      playButton.classList.add("fc-paused");
    } else {
      playButton.classList.remove("fc-paused");
      playButton.classList.add("fc-playing");
    }
  };


  // Set current source for audio to given track number
  fcPlayer.prototype.loadTrack = function (trackNumber) {
    var source = this.fcaudio.getElementsByTagName("source").item(trackNumber).getAttribute('src');
    this.fcaudio.src = source;
    // don't autoplay if fcplayer state is paused
    if (this.state === 'paused') {
      this.fcaudio.pause();
    } 
    this.currentTrack = trackNumber;
    this.log('func: loadTrack: loaded ' + source);
  };


  // Load next track in playlist
  fcPlayer.prototype.loadNext = function () {
    this.log('func: loadNext');
    var trackCount = this.fcaudio.getElementsByTagName("source").length;
    var newTrack   = ((1 + this.currentTrack) % trackCount);
    if (newTrack <= this.currentTrack && !this.repeat) {
      this.state = "paused";
    }
    this.loadTrack(newTrack);
  };


  // Load previous track in playlist
  fcPlayer.prototype.loadPrevious = function () {
    this.log('func: loadPrevious');
    var trackCount = this.fcaudio.getElementsByTagName('source').length;
    var newTrack = (this.currentTrack + (trackCount - 1)) % trackCount;
    this.loadTrack(newTrack);
  };


  // Set up event handlers for audio element events
  fcPlayer.prototype.setAudioEventHandlers = function () {

    var self = this;
    self.log('func: setAudioEventHandlers');

    self.fcaudio.addEventListener('abort', function () {
      self.log('event: audio abort');
    });

    // Update display and continue play when song has loaded
    self.fcaudio.addEventListener('canplay', function () {//doubt - way of defining or calling function
      self.log('event: audio canplay');
      if (self.state === 'playing' && this.paused) {
        this.play();
      }
      self.updateDisplay();
    });

    self.fcaudio.addEventListener('canplaythrough', function () {
      self.log('event: audio canplaythrough');
    });

    self.fcaudio.addEventListener('durationchange', function () {
      self.log('event: audio durationchange');
    });

    self.fcaudio.addEventListener('emptied', function () {
      self.log('event: audio emptied');
    });

    // Load next track when current one ends
    self.fcaudio.addEventListener('ended', function () {
      self.log('event: audio ended');
      self.loadNext();
    });

    self.fcaudio.addEventListener('error', function () {
      self.log('event: audio error');
    });

    self.fcaudio.addEventListener('loadeddata', function () {
      self.log('event: audio loadeddata');
    });

    self.fcaudio.addEventListener('loadedmetadata', function () {
      self.log('event: audio loadedmetadata');
    });

    self.fcaudio.addEventListener('loadstart', function () {
      self.log('event: audio loadstart');
    });

    self.fcaudio.addEventListener('pause', function () {
      self.log('event: audio pause');
    });

    self.fcaudio.addEventListener('play', function () {
      self.log('event: audio play');
    });

    self.fcaudio.addEventListener('playing', function () {
      self.log('event: audio playing');
    });

    self.fcaudio.addEventListener('progress', function () {
      self.log('event: audio progress');
    });

    self.fcaudio.addEventListener('ratechange', function () {
      self.log('event: audio ratechange');
    });

    self.fcaudio.addEventListener('seeked', function () {
      self.log('event: audio seeked');
    });

    self.fcaudio.addEventListener('seeking', function () {
      self.log('event: audio seeking');
    });

    self.fcaudio.addEventListener('stalled', function () {
      self.log('event: audio stalled');
    });

    self.fcaudio.addEventListener('suspend', function () {
      self.log('event: audio suspend');
    });

    self.fcaudio.addEventListener('timeupdate', function () {
      // self.log('event: audio timeupdate');
      self.updateDisplay();
    });

    self.fcaudio.addEventListener('volumechange', function () {
      self.log('event: audio volumechange');
    });

    self.fcaudio.addEventListener('waiting', function () {
      self.log('event: audio waiting');
    });

  };



  // Set up button click handlers
  fcPlayer.prototype.setClickHandlers = function () {

    var self = this;
    self.log('func: setClickHandlers');
    var audioElem = self.fcaudio;

    // Activate fast-forward
    [].forEach.call(
      self.fcplayer.getElementsByClassName('fc-forward'),
      function (el) {
        el.addEventListener('click', function () {
          self.log('event: click .fc-forward');
          self.loadNext();          
        });
      }
    );

    // Toggle play / pause
    [].forEach.call(
      self.fcplayer.getElementsByClassName('fc-play'),
      function (el) {
        el.addEventListener('click', function () {
          self.log('event: click .fc-play');
          if (self.fcaudio.paused) { //(audioElem.paused) {
            stopAllfcPlayers();
            self.fcaudio.play();
            self.state = "playing";
          } else {
            self.fcaudio.pause();
            self.state = "paused";
          }
          self.updateDisplay();
        });
      }
    );

    // Activate rewind
    [].forEach.call(
      self.fcplayer.getElementsByClassName('fc-rewind'),
      function (el) {
        el.addEventListener('click', function () {
          self.log('event: click .fc-rewind');
          var time = audioElem.currentTime;
          if (time > 1.5) {
            audioElem.currentTime = 0;
          } else {
            self.loadPrevious();
          }
        });
      }
    );


    // TODO make debug more "pluggy".
    if (self.fcdebug) {
      self.fcdebug.click(function () {
        $(this).empty();//doubt: why paranthesis around this
      });
    }

  };




  // fcPlayer initialisation
  fcPlayer.prototype.init = function () {
    var self = this;
    self.setAudioEventHandlers();
    self.loadSources();
    self.currentTrack = 0;
    self.setClickHandlers();
    self.updateDisplay();
  };



  // Create fcPlayer Object for each element of .fcplayer class
  document.addEventListener('DOMContentLoaded', function() {
    [].forEach.call(
      document.getElementsByClassName("fcplayer"),
      function (el) {
        fcplayers.push(new fcPlayer(el));
      }
    );
  });

}());
