import { FormGroup } from '@angular/forms';



// custom validator which ensures that two form fields match
export function MustMatch(fieldName: string, matchingFieldName: string) {
	return(formGroup: FormGroup) => {
		const field = formGroup.controls[fieldName];
		const matchingField = formGroup.controls[matchingFieldName];
		
		// returns null if iff fields have not yet initialized
		if (!field || !matchingField) {
			return null;
		}
		
		// returns null iff matchingField was caught by other validators
		if (matchingField.errors && !matchingField.errors.mustMatch) {
			return null;
		}
		
		// sets error status on matchingField
		if (field.value !== matchingField.value) {
			matchingField.setErrors({ mustMatch: true });
		} else {
			matchingField.setErrors(null);
		}
	}
}