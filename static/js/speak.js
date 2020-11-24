var speechVoiceAvailbale = {
    "ja" : undefined,
    "th" : undefined,
    "en" : undefined,
}

speechSynthesis.onvoiceschanged = function() {
    // loop for each language (jp, th, en)
    $.each(speechVoiceAvailbale, function(targetLang, __v) {
        // loop for browser-available-voices
        $.each(speechSynthesis.getVoices(), function(__index, voice) {
            if(voice.lang.startsWith(targetLang)){
                // set available voice for target language
                speechVoiceAvailbale[targetLang] = voice;
                return false;
            }
        });
    });

    // set speakbale indicator
    setSpeakableOrNot();
}

function setSpeakableOrNot() {
    $.each(speechVoiceAvailbale, function(lang, v) {
        var target = $('.speech-button-' + lang);
        // set/unset speakable indicator
        if(v) {
            target.find('.speech-target').addClass('speakable');
        } else {
            target.find('.speech-target').removeClass('speakable');
        }
    });
}

$(document).ready(function() {
    // first set the voices
    speechSynthesis.onvoiceschanged();

    var all_target_class = Object.keys(speechVoiceAvailbale).map(k => '.speech-button-' + k).join(', ');
    $(document).on('click', all_target_class, function() {
        var self = this;
        var voice;
        $.each(speechVoiceAvailbale, function(lang, v) {
            if($(self).is('.speech-button-' + lang)){
                voice = v;
                return false;
            }
        });
        if(!voice) {
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
        msg.lang = voice.lang;
        msg.voice = voice;
        msg.text = text;
        msg.rate = 0.8; // speed (min 0 - max 10)
        
        // speak (if already speaking, cancel it)
        speechSynthesis.cancel();
        speechSynthesis.speak(msg);
    });
});
