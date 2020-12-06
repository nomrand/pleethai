var SPEECH_VOICE_AVAILBALE = {
    "ja" : {
        "voice": undefined,
        "lang": "ja-JP"
    },
    "th" : {
        "voice": undefined,
        "lang": "th-TH"
    },
    "en" : {
        "voice": undefined,
        "lang": "en-US"
    },
};

window.speechSynthesis.onvoiceschanged = function(e) {
    loadVoices();
};

function loadVoices() {
    // loop for each language (jp, th, en)
    $.each(SPEECH_VOICE_AVAILBALE, function(targetLang, __v) {
        // loop for browser-available-voices
        $.each(window.speechSynthesis.getVoices(), function(__index, voice) {
            if(voice.lang.startsWith(targetLang)){
                // set available voice for target language
                SPEECH_VOICE_AVAILBALE[targetLang].voice = voice;
                return false;
            }
        });
    });

    // set speakbale indicator
    setSpeakableOrNot();
}

function setSpeakableOrNot() {
    $.each(SPEECH_VOICE_AVAILBALE, function(lang, v) {
        var target = $('.speech-button-' + lang);
        // set/unset speakable indicator
        if(v.voice) {
            target.find('.speech-target').addClass('speakable');
            // this is for click event bug of iOS
            target.css({'cursor': 'pointer'});
        } else {
            target.find('.speech-target').removeClass('speakable');
            target.css({'cursor': 'inherit'});
        }
    });
}

$(window).on('load', function() {
    // first set the voices
    loadVoices();

    var all_target_class = Object.keys(SPEECH_VOICE_AVAILBALE).map(function(k){
        return '.speech-button-' + k;
    }).join(', ');
    $(document).on('click', all_target_class, function() {
        // if voice is already speaking, do nothing
        if(window.speechSynthesis.pending || window.speechSynthesis.speaking){
            return;
        }

        var self = this;
        var voiceObj;
        $.each(SPEECH_VOICE_AVAILBALE, function(lang, v) {
            if($(self).is('.speech-button-' + lang)){
                voiceObj = v;
                return false;
            }
        });
        if(!voiceObj) {
            return false;
        }

        // find speak word
        var base = $(self).find('.speech-target');
        var text = base.text();
        if(base.attr('data-text')){
            text = base.attr('data-text');
        }

        // set speak setting
        var msg = new SpeechSynthesisUtterance();
        if(voiceObj.voice){
            msg.lang = voiceObj.lang;
            msg.voice = voiceObj.voice;
        } else {
            // In MacOS, some times getVoices returns voice object which has empty lang,
            // then try to speech with default lang 
            msg.lang = voiceObj.lang;
        }
        msg.text = text;
        msg.rate = 0.8; // speed (min 0 - max 10)

        // speak
        $(msg).on('end error', function() {
            base.removeClass('speaking');
        });
        base.addClass('speaking');
        window.speechSynthesis.speak(msg);
    });
});
