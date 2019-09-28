let pattern = /xyz/;
console.log(pattern);
console.log(typeof pattern);
let value = 'this is xyz a test';
console.log(pattern.test(value));
console.log(value.replace(pattern, 'abc'));
console.log(pattern.test(value));
console.log(value.match(pattern));
let match = value.match(pattern);
console.log(match.input);

// Email address validator

let mailPattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
let dummyMail = 'mailmahmudnotes.com';
if (mailPattern.test(dummyMail)) {
    console.log('Email submitted successfully');
} else {
    console.log('Please enter a valid email address.');
}
